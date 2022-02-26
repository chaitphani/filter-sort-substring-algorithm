from rest_framework import serializers
from .models import UserData


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'


class UserDataUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['first_name', 'last_name', 'age']