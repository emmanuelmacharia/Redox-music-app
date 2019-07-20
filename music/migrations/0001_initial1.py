# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-05 12:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=50)),
                ('album_Title', models.CharField(max_length=300)),
                ('album_Year', models.CharField(max_length=20)),
                ('genre', models.CharField(max_length=50)),
                ('album_art', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=100)),
                ('song_title', models.CharField(max_length=100)),
                ('song_lyrics', models.CharField(max_length=1500)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Albums')),
            ],
        ),
    ]
