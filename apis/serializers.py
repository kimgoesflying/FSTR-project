from rest_framework import serializers
from mountain_pass.models import MountainPass, Tourist, MountainPassImage
from drf_writable_nested.serializers import WritableNestedModelSerializer
from base64 import b64encode, b64decode


class Base64BinaryField(serializers.Field):
    def to_representation(self, value):
        return b64encode(value)

    def to_internal_value(self, data):
        return b64decode(data)


class TouristSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist
        fields = ('email', 'first_name', 'middle_name', 'last_name', 'phone')


class MountainPassImageSerializer(serializers.ModelSerializer):
    image_base64 = Base64BinaryField(source='binary_image')

    class Meta:
        model = MountainPassImage
        fields = ('image_base64', 'title')


class MountainPassSerializer(WritableNestedModelSerializer):
    user = TouristSerializer()
    images = MountainPassImageSerializer(many=True)

    class Meta:
        model = MountainPass
        fields = ('title', 'other_titles',
                  'beauty_title',
                  'connect',  'status', 'user',
                  'latitude', 'longitude', 'height',
                  'level_winter', 'level_spring',
                  'level_summer', 'level_autumn',
                  'images'
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
