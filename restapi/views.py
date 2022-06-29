from django.shortcuts import render
from rest_framework.views import APIView
from restapi.models import Todos
from restapi.serializers import TodoSerializer
from rest_framework.response import Response


# Create your views here.
#todo create,detail,list,update,delete
class TodosView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Todos.objects.all()
        serializer=TodoSerializer(qs,many=True)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
class TodoDetails(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("todo_id")
        todo=Todos.objects.get(id=id)
        serializer=TodoSerializer(todo)
        return Response(serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("todo_id")
        todo=Todos.objects.get(id=id)
        serializer=TodoSerializer(instance=todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("todo_id")
        todo=Todos.objects.get(id=id)
        todo.delete()
        return Response({"msg":"deleted"})

