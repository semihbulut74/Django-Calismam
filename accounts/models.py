from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class KullaniciProfili(models.Model):
    kullanici =models.OneToOneField(User)
    aciklama= models.CharField(max_length=100, default='')
    sehir =models.CharField(max_length=100, default='')
    websayfa =models.URLField(default='')
    telefon =models.IntegerField(default=0)

