# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-12 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_textfieldchange'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='song_lyrics',
            field=models.TextField(max_length=15000),
        ),
    ]
