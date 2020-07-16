from rest_framework import serializers
from .models import *



class ImageSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['name', 'img']

        