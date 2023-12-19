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


class Article(models.Model):
    STATUS_CHOICES = [
        (0, 'in progress'),
        (1, 'wait for acceptance'),
        (2, 'published')
    ]

    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64, null=True)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES)
    emission_start = models.DateField(null=True)
    emission_end = models.DateField(null=True)


class Album(models.Model):
    RATING_CHOICES = [
        (0, '0 stars'),
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    ]

    title = models.CharField(max_length=128)
    year = models.IntegerField()
    rating = models.IntegerField(choices=RATING_CHOICES)
