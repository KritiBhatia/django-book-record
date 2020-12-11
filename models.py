from django.db import models
from django.contrib.auth.models import User

class Book(models.Model): #inheriting Model class
    title=models.CharField(max_length=100)
    price=models.FloatField()
    author=models.CharField(max_length=100)
    publisher=models.CharField(max_length=100)

class DBRuser(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE) #mapped with Django User table
    nickname=models.CharField(max_length=20, null=False)
