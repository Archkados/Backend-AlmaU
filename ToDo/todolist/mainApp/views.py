from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.

class ListTodo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializers


class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializers

class CreateTodo(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializers

class DeleteTodo(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializers
