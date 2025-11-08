from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=254, unique=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=254)
    precio=models.IntegerField()
    categoria=models.ManyToManyField(Categoria)
    imagen=models.ImageField(upload_to="productos")

    def __str__(self):
        return self.nombre


class Inventario(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.producto.nombre} - Stock: {self.stock}"
