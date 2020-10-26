from django.urls import path
from my_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('player/create', views.PlayerCreateView.as_view(), name='player_create'),
    path('player/<int:pk>/detail', views.PlayerDetailView.as_view(), name='player_detail'),
    path('team/create', views.TeamCreateView.as_view(), name='team_create'),
    path('team/<int:pk>/detail', views.TeamDetailView.as_view(), name='team_detail'),
    path('team/join', views.join_team, name='team_join'),
    path('user/<int:pk>/detail', views.UserDetailView.as_view(), name='user_detail'),
    path('signup', views.signup, name='signup'),
    path('about', views.about, name='about'),
    path('squad/<str:team_name>/pick', views.squad_picker, name='squad_picker')
]
