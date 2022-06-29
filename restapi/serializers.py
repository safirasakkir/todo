from rest_framework.serializers import ModelSerializer
from restapi.models import Todos
from rest_framework import serializers

class TodoSerializer(ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Todos
        fields=["id","task_name","user","status"]