from dataclasses import field
from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

# create serializers here


class TaskSerlialization(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'task_date']

# User Serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        return user
