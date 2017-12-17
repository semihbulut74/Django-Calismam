from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import  post_save

# Create your models here.

class KullaniciProfili(models.Model):
    kullanici =models.OneToOneField(User)
    aciklama= models.CharField(max_length=100, default='')
    sehir =models.CharField(max_length=100, default='')
    websayfa =models.URLField(default='')
    telefon =models.IntegerField(default=0)

def profil_olustur(sender, **kwargs):
    if kwargs['created']:
        user_profile =KullaniciProfili.objects.create(kullanici=kwargs['instance'])

post_save.connect(profil_olustur, sender=User)

