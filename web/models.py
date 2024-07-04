import datetime
from django.db import models
from distutils.command.upload import upload
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id Categoria') 
    nombreCategoria= models.CharField(max_length=50, verbose_name='Nombre Categoria')

    def __str__(self):
        return self.nombreCategoria

class Photocard(models.Model):
    idPhotocard = models.CharField(primary_key=True, max_length=10, verbose_name='Id Photocard')
    marca = models.CharField(max_length=40, verbose_name='Marca')
    modelo = models.CharField(max_length=40, verbose_name='Modelo')
    imagen = models.ImageField(upload_to="imagenes", null=True, verbose_name='Imagen')
    categoria = models.ForeignKey('Categoria', default=1,on_delete=models.CASCADE, verbose_name='Categoria')
    precio = models.IntegerField(blank=True, null=True, verbose_name="Precio")
    stock = models.IntegerField(default=0, verbose_name='Stock')

    def __str__(self):
        return self.idPhotocard
    
class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True)
    total=models.BigIntegerField()
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)
  
    def __str__(self):
        return str(self.id_boleta)

class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Photocard', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)
    
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=30, default='cliente')

    def __str__(self):
        return self.user.username
    
if not Group.objects.filter(name='cliente').exists():
    Group.objects.create(name='cliente')