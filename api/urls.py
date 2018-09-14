from django.conf.urls import url, include
from django.urls import path
from api import views

urlpatterns = [
    path('', views.ListTodo.as_view()),
    path('<int:pk>/', views.DetailTodo.as_view())
]
