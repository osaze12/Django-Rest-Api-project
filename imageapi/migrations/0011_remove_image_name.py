# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-16 01:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imageapi', '0010_auto_20200716_0248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
    ]
