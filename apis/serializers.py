from rest_framework import serializers
from mountain_pass.models import MountainPass, Tourist, Coordinates, MountainPassImage


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

        fields = '__all__'


class MountainPassSerializer(serializers.ModelSerializer):
    user = TouristSerializer()
    coords = CoordinatesSerializer(source='coordinates')
    level_winter = serializers.ChoiceField(
        source='lvl_winter', choices=MountainPass.LEVEL_TYPE)
    level_spring = serializers.ChoiceField(
        source='lvl_spring', choices=MountainPass.LEVEL_TYPE)
    level_summer = serializers.ChoiceField(
        source='lvl_summer', choices=MountainPass.LEVEL_TYPE)
    level_autumn = serializers.ChoiceField(
        source='lvl_autumn', choices=MountainPass.LEVEL_TYPE)
    status = serializers.ChoiceField(choices=MountainPass.STATUS_TYPE)
    images = MountainPassImageSerializer(many=True)

    class Meta:
        model = MountainPass
        # fields = '__all__'
        fields = ('title', 'other_titles',
                  'connect',  'status',
                  'user', 'coords',
                  'level_winter', 'level_spring',
                  'level_summer', 'level_autumn', 'images')
