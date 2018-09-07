from django.db import models
from django.conf import settings

# Create your models here.

class ToDo(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=20, null=False)
    description = models.TextField(max_length=144, null=True)
    archived = models.BooleanField(default=False, null=False)

