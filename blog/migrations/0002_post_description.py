# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='GCECT', max_length=400),
        ),
    ]
