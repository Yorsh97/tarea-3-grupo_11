from django.db import models

# Create your models here.
class Proveedores(models.Model):
	nombre=models.CharField(max_length=30)
	rut=models.IntegerField()
	direccion=models.CharField(max_length=256)
	telefono=models.IntegerField()

class Productos(models.Model):
	categoria=models.CharField(max_length=30)
	cantidad = models.CharField(max_length=30)
	nombre=models.CharField(max_length=30)
	codigo=models.IntegerField()
	precio=models.IntegerField()
	proveedores=models.ForeignKey(Proveedores, on_delete=models.CASCADE)

class Clientes(models.Model):
	nombreCompleto=models.CharField(max_length=128)
	rut=models.IntegerField()
	fechaNacimiento=models.DateField()
	direccion=models.CharField(max_length=256)
	correo=models.CharField(max_length=256)
	telefono=models.IntegerField()

class Pedidos(models.Model):
	productos=models.ForeignKey(Productos, on_delete=models.CASCADE)
	clientes=models.ForeignKey(Clientes, on_delete=models.CASCADE)
	fueEntregado=models.BooleanField(default=False)
	fechaPedido=models.DateField()
	fechaDespacho=models.DateField()

	

	