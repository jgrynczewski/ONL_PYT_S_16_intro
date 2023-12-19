from django.db import models


# Create your models here.
class Band(models.Model):
    CHOICES = [
        (-1, 'not defined'),
        (0, 'rock'),
        (1, 'metal'),
        (2, 'pop'),
        (3, 'hip - hop'),
        (4, 'electronic'),
        (5, 'reggae'),
        (6, 'other')
    ]

    name = models.CharField(max_length=64)
    year = models.IntegerField(null=True)
    still_active = models.BooleanField(default=True)
    genre = models.IntegerField(choices=CHOICES, default=-1)


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)
