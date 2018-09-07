from django.urls import path, include
from todo.views import createToDo, archiveToDo, deleteToDo

urlpatterns = [
    path('create', createToDo, name='create'),
    path('archive', archiveToDo, name='archive'),
    path('delete', deleteToDo, name='delete')
]
