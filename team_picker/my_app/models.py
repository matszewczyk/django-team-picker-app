from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('player_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    members = models.ManyToManyField(User, through='Membership')
    password = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('team_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name


class Membership(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('player', 'team')
