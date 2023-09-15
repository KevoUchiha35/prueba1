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

class contactanos(models.Model):
    nombre = models.CharField(max_length=250, null=True)
    apellido = models.CharField(max_length=250, null=True)
    nickname = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250, null=True, unique=False) 
    asunto = models.CharField(max_length=250, null=True, unique=False) 

class tienda(models.Model):
    user = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name='tienda', null=True)
    nombre = models.CharField(max_length=250, null=True)
    apellido = models.CharField(max_length=250, null=True)
    correo = models.CharField(max_length=250, null=True, unique=False)
    numero = models.CharField(max_length=250, null=True, unique=False)
    direccion = models.CharField(max_length=250, null=True, unique=False)
    pago = models.BooleanField(default=False,null=True)
    total = models.CharField(max_length=250, null=True, unique=False)

class Noticias  (models.Model):
    
    titulo = models.CharField(max_length=90)
    contenido = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="noticias", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)


    class Meta:
       
        verbose_name= "noticia" 
        verbose_name_plural= "noticias"
    


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="productos", null=True)
    def _str_(self): 
        return self.nombre 

  #salida 
    def _str_(self):
        return self.titulo
    
class Datosuser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True)
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    correo = models.EmailField(max_length=250, null=True, unique=False)
    numero = models.CharField(max_length=250, null=True, unique=False)
    direccion = models.CharField(max_length=250, null=True, unique=False)

class Meta:
    verbose_name_plural = 'Informacion Personal'
    
