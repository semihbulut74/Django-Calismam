# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-17 16:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='KullaniciProfili',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aciklama', models.CharField(default='', max_length=100)),
                ('sehir', models.CharField(default='', max_length=100)),
                ('websayfa', models.URLField(default='')),
                ('telefon', models.IntegerField(default=0)),
                ('kullanici', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
