from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions

from .serializers import *
from .models import *


class TouristViewset(viewsets.ModelViewSet):
    queryset = Tourist.objects.all()
    serializer_class = TouristSerializer

    def list(self, request, format=None):
        return Response([])
