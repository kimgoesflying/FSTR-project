from .models import Tourist
from rest_framework import serializers


class TouristSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tourist
        fields = ['id', 'get_full_name', 'email', 'phone']
