from django.db import models
from usuarios.models import Usuario
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
        return self.producto.nombre, self.stock

class Venta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    costo_total_sin_iva = models.FloatField()
    costo_total_con_iva = models.FloatField()
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.nombre_completo

class Detalle_venta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.IntegerField()

    def __str__(self):
        return self.producto.nombre
    
    @property
    def subtotal(self):
        return self.precio_unitario * self.cantidad
