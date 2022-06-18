from inspect import classify_class_attrs
from operator import mod
from django.db import models

class Login(models.Model):
    name=models.CharField(max_length=50)
    passwords= models.CharField(max_length=50)