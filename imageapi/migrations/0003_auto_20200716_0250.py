# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-16 01:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapi', '0002_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to='media', verbose_name='file'),
        ),
    ]