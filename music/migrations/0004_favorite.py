# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-13 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_textfieldlength'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
