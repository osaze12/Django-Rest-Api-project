# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import api_view
from .models import *
from imageapi.serializers import ImageSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FormParser, MultiPartParser



# Create your views here.


@api_view(['GET'])
def image_list(request, format=None):
    all_img = Image.objects.all()
    serialize = ImageSerializers(all_img, context={'request': request},  many=True)
    return Response(serialize.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload(request):
    serializer = ImageSerializers(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def image(request, id):
    try:
        img = Image.objects.get(id= id)
        serialize = ImageSerializers(img, many=False)
        return Response(serialize.data, status=status.HTTP_200_OK)
    except Image.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



