from django.shortcuts import render, redirect
from todo.models import ToDo

# Create your views here.

def createToDo(request):

    if (request.POST):
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        archived = False
        todo = ToDo(user=user, title=title, description=description, archived=archived)
        todo.save()

    return redirect('/webpage')

def archiveToDo(request):

    if (request.POST):

        todo = ToDo.objects.get(id=request.POST.get('id'))

        if (request.user == todo.user):
            todo.archived = True
            todo.save()

    return redirect('/webpage')

def deleteToDo(request):
    print(request)
    if (request.POST):

        todo = ToDo.objects.get(id=request.POST.get('id'))

        if (request.user == todo.user):
            todo.delete()

    return redirect('/webpage')