from rest_framework import generics
from todo.models import ToDo
from api.serializers import ToDoSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer