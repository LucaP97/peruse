from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from .models import *

### PROFILES ###

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

class ProfileRegistrationSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        
        user_serializer = UserCreateSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        return Profile.objects.create(user=user, **validated_data)
    
    class Meta:
        model = Profile
        fields = ['id', 'user', 'location', 'nickname']

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'location', 'nickname']