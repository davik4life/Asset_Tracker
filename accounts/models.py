from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from rest_framework import viewsets, permissions
# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
