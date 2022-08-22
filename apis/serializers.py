from rest_framework import serializers
from mountain_pass.models import MountainPass, Tourist, Coordinates, MountainPassImage
from drf_writable_nested.serializers import WritableNestedModelSerializer


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = ('latitude', 'longitude', 'height')


class TouristSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist
        fields = ('email', 'first_name', 'middle_name', 'last_name', 'phone')


class MountainPassImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountainPassImage
        fields = ('image', 'title')


class MountainPassSerializer(WritableNestedModelSerializer):
    user = TouristSerializer()
    coords = CoordinatesSerializer(source='coordinates')

    class Meta:
        model = MountainPass
        fields = ('title', 'other_titles',
                  'connect',  'status', 'user',
                  'coords',
                  'level_winter',
                  'level_spring', 'level_summer',
                  'level_autumn',
                  # 'images'
                  )
