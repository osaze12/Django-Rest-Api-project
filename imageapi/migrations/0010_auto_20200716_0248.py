# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-16 01:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('imageapi', '0009_remove_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='image',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media', verbose_name='file'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default='no value', max_length=80),
        ),
    ]
