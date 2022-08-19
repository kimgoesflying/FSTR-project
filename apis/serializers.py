from rest_framework import serializers
from mountain_pass.models import MountainPass, Tourist, Coordinates


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates

        fields = '__all__'


class TouristSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist

        fields = '__all__'


class MountainPassSerializer(serializers.ModelSerializer):
    tourist = TouristSerializer(source='user', read_only=True)
    cords = CoordinatesSerializer(source='coords', read_only=True)

    class Meta:
        model = MountainPass
        # fields = '__all__'
        fields = ('title', 'other_titles',
                  'connect',  'status', 'tourist', 'cords')
