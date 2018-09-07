from django.shortcuts import render
from todo.models import ToDo

# Create your views here.

def index(request):

    context = {'todos' : ToDo.objects.all().filter(archived=False, user=request.user)}

    return render(request, 'webpage/index.html', context)