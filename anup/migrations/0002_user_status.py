# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-24 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.IntegerField(default=0, max_length=20),
        ),
    ]