from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from importlib.resources import contents
from sqlite3 import Timestamp
from time import time, timezone
# Create your models here.
class jugadores(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True)
    nombre = models.CharField(max_length=250, null=True)
    apellido = models.CharField(max_length=250, null=True)
    nickname = models.CharField(max_length=250, null=True)
    nacimiento = models.CharField(max_length=250, null=True)
    correo = models.CharField(max_length=250, null=True, unique=False)
    redsocial = models.CharField(max_length=250, null=True, unique=False)
    videojuegofav = models.CharField(max_length=250, null=True, unique=False)
    plataforma_xbox = models.BooleanField(default=False,null=True)