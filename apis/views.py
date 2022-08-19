from rest_framework import generics

from mountain_pass import models
from .serializers import MountainPassSerializer


class ListMountainPass(generics.ListCreateAPIView):
    queryset = models.MountainPass.objects.all()
    serializer_class = MountainPassSerializer


class DetailMountainPass(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MountainPass.objects.all()
    serializer_class = MountainPassSerializer
