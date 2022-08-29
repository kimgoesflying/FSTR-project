from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from mountain_pass import models
from .serializers import MountainPassSerializer


class ListMountainPass(APIView):

    def get(self, request):
        mountain_pass_list = models.MountainPass.objects.all()
        serializer = MountainPassSerializer(mountain_pass_list, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = MountainPassSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailMountainPass(APIView):
    def get(self, request, pk):
        try:
            mountain_pass = models.MountainPass.objects.get(pk=pk)
        except models.MountainPass.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MountainPassSerializer(mountain_pass)
        return Response(serializer.data)

    def patch(self, request, pk):

        mountain_pass = models.MountainPass.objects.get(pk=pk)
        mountain_pass_status = mountain_pass.status
        if mountain_pass_status == 'new':
            request.data.pop('user')

            serializer = MountainPassSerializer(
                mountain_pass, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({'state': 1, 'message': "Success"}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'state': 0, 'message': f"Cant edit {mountain_pass_status} status"}, status=status.HTTP_204_NO_CONTENT)
