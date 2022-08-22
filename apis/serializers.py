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

    def validate_status(self, value):
        STATUS_TYPE = [
            'new',
            'pending',
            'accepted',
            'rejected',
        ]

        if value in STATUS_TYPE:
            return value
        else:
            raise serializers.ValidationError(
                "status can only be 'new, 'pending', accepted' or 'rejected'")

    LEVEL_TYPE = ['1А', '1Б', '1Б*', '2А',
                  '2Б*', '2Б', '3А', '3Б', '3Б*', '']

    def validate_level_winter(self, value):
        if value in self.LEVEL_TYPE:
            return value
        else:
            raise serializers.ValidationError(
                "Level can only be '1А', '1Б', '1Б*', '2А', '2Б*', '2Б', '3А', '3Б', '3Б * or empty string")

    def validate_level_spring(self, value):
        if value in self.LEVEL_TYPE:
            return value
        else:
            raise serializers.ValidationError(
                "Level can only be '1А', '1Б', '1Б*', '2А','2Б*', '2Б', '3А', '3Б', '3Б*")

    def validate_level_summer(self, value):
        if value in self.LEVEL_TYPE:
            return value
        else:
            raise serializers.ValidationError(
                "Level can only be '1А', '1Б', '1Б*', '2А','2Б*', '2Б', '3А', '3Б', '3Б*")

    def validate_level_autumn(self, value):
        if value in self.LEVEL_TYPE:
            return value
        else:
            raise serializers.ValidationError(
                "Level can only be '1А', '1Б', '1Б*', '2А','2Б*', '2Б', '3А', '3Б', '3Б*")
