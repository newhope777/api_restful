from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=25, default=None) 
    origin = models.CharField(max_length=25, default=None)
    band = models.CharField(max_length=30, default=None)

class Album(models.Model):
    title = models.CharField(max_length=40, default=None)
    style = models.CharField(max_length=30, default=None)
    year = models.DateTimeField('release year')

class Song(models.Model):
    title = models.CharField(max_length=40, default=None)
    lyrics = models.CharField(max_length=500, default=None)
