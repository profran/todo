from django.urls import path, include
from todo.views import createToDo, archiveToDo, deleteToDo

urlpatterns = [
    path('create', createToDo),
    path('archive', archiveToDo),
    path('delete', deleteToDo)
]
