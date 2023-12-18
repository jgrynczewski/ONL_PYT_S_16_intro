from django.db import models


class Game(models.Model):
    id = models.BigAutoField(primary_key=True)
    team_home = models.ForeignKey('Team', blank=True, null=True, related_name='games_home', on_delete=models.CASCADE)
    team_home_goals = models.BigIntegerField(blank=True, null=True)
    team_away = models.ForeignKey('Team', blank=True, null=True, related_name='games_away', on_delete=models.CASCADE)
    team_away_goals = models.BigIntegerField(blank=True, null=True)


class Team(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    points = models.BigIntegerField(blank=True, null=True)
