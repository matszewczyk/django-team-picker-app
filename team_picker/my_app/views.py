from django.shortcuts import render, redirect
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from my_app import views
from my_app.models import Player,Team
from my_app.forms import PlayerForm, TeamForm, MembershipForm

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return render(request, 'my_app/index.html')


class PlayerListView(ListView):
    model = Player


class PlayerDetailView(DetailView):
    model = Player


class PlayerCreateView(CreateView, LoginRequiredMixin):
    login_url = '/login/' # where to go when someone is not logged in
    model = Player
    form_class = PlayerForm


class TeamListView(ListView):
    model = Team


class TeamDetailView(DetailView):
    model = Team


class TeamCreateView(LoginRequiredMixin,CreateView):
    model = Team
    fields = ['name', 'password']
    login_url = '/accounts/login/' # where to go when someone is not logged in


class UserDetailView(DetailView):
    model = User
    template_name = 'my_app/user_detail.html'


@login_required(login_url="/accounts/login/")
def join_team(request):
    if request.method == 'POST':
        form = MembershipForm(request.POST, initial={'player': request.user})
        if form.is_valid():
            team = form.cleaned_data['team']
            password = form.cleaned_data['password']
            real_password = Team.objects.get(name=team).password
            if password == real_password:
                form.save(commit=True)
                return redirect('user_detail', pk=request.user.pk)
            else:
                form.errors['__all__'] = form.error_class(['Wrong password supplied!'])
        else:
            render(request, 'my_app/join_team.html', {'error': form.errors})

    else:
        form = MembershipForm(initial={'player': request.user})

    return render(request, 'my_app/join_team.html', {'form': form})

def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect ('index')
    else:
        form = UserCreationForm()
    return render(request, 'my_app/signup.html', {'form':form})

def about(request):
    return render(request, 'my_app/about.html')

def squad_picker(request, team_name):
    team = Team.objects.get(name=team_name)
    return render(request, 'my_app/squad_picker.html', {'team':team})