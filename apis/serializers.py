from rest_framework import serializers
from mountain_pass.models import Tourist


class TouristSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist
        fields = ('id', 'first_name', 'middle_name',
                  'last_name',  'email', 'phone')
