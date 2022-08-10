from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model) :
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=255)
    task_date=models.DateField()
   
