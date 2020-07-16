# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Image(models.Model):
    name = models.CharField(max_length=80, default='no value')
    img = models.ImageField(verbose_name='file', upload_to='uploads')
    date_created = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name


# class Transformed(model.Model):
#     name = models.CharField(max_length=80, default='no value')
#     img = models.ImageField(verbose_name='file', upload_to='transformed')
#     date_created = models.DateTimeField(auto_now=True)