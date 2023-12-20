from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100)


# One-to-one
class Country(models.Model):
    name = models.CharField(max_length=64)
    capital = models.OneToOneField('Capital', on_delete=models.CASCADE)


class Capital(models.Model):
    name = models.CharField(max_length=64)


# One-to-many
class Language(models.Model):
    name = models.CharField(max_length=64)


class Framework(models.Model):
    name = models.CharField(max_length=64)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)


# Many-to-many
class Actor(models.Model):
    name = models.CharField(max_length=128)


class Movie(models.Model):
    name = models.CharField(max_length=128)
    actors = models.ManyToManyField("Actor")
