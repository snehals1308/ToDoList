from django.db import models

# Create your models here.
class todo(models.Model):
    datetime = models.DateTimeField()
    name = models.CharField(max_length=200)
    todolist = models.TextField()
    