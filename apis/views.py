from rest_framework import generics

from mountain_pass import models
from .serializers import TouristSerializer


class ListTourists(generics.ListCreateAPIView):
    queryset = models.Tourist.objects.all()
    serializer_class = TouristSerializer


class DetailTourist(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Tourist.objects.all()
    serializer_class = TouristSerializer
