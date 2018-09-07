from django.urls import path, include
from webpage.views import index

urlpatterns = [
    path('', index)
]
