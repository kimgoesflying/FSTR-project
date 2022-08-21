from rest_framework import generics
from rest_framework.response import Response


from mountain_pass import models
from .serializers import MountainPassSerializer


class ListMountainPass(generics.ListCreateAPIView):
    queryset = models.MountainPass.objects.all()
    serializer_class = MountainPassSerializer

    def get(self, request):
        objs = models.MountainPass.objects.all()
        serializer = MountainPassSerializer(objs, many=True)

        return Response(serializer.data)


class DetailMountainPass(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MountainPass.objects.all()
    serializer_class = MountainPassSerializer
