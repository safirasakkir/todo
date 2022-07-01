from rest_framework.serializers import ModelSerializer
from restapi.models import Todos
from rest_framework import serializers
from django.contrib.auth.models import User


class TodoSerializer(ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Todos
        fields=["id","task_name","user","status"]

class Userserializer(ModelSerializer):
    id=serializers.CharField(read_only=True)

    class Meta:
        model=User
        fields=["id","first_name","last_name","username","email","password"]
#to use this create_user method for password hashing that means hide password
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()