from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import manager

#para trabajar con fechas
import datetime
from django.utils import timezone

# Create your models here.

class Ingrediente(models.Model):
    ingrediente_id = models.IntegerField(primary_key=True)
    nom_ingrediente = models.CharField(max_length=25)

    def __str__(self):
        return self.nom_ingrediente

class Pizza(models.Model):

	pizza_id = models.IntegerField(primary_key=True)
	nom_pizza = models.CharField(max_length=30)
	precio = models.FloatField()
	objects = models.Manager()

	def __str__(self):
		return self.nom_pizza

class TipoMasa(models.Model):

	tipo_masa_id = models.IntegerField(primary_key=True)
	nom_tipo = models.CharField(max_length=7)

	def __str__(self):
		return self.nom_tipo

class Hecha_De(models.Model):
	corr_hec_de=models.AutoField(primary_key=True)
	pizza=models.ForeignKey(Pizza,on_delete=models.CASCADE)
	ingrediente=models.ForeignKey(Ingrediente,on_delete=models.CASCADE)
	tipomasa=models.ForeignKey(TipoMasa,on_delete=models.CASCADE)

	def __str__(self):
		pass
		
#nuevos
class Empleado(models.Model):
	cod_empleado=models.IntegerField(primary_key=True)
	nom_empleado=models.CharField(max_length=40)
	password_empleado=models.CharField(max_length=16,blank=False)

	def __str__(self):
		return self.nom_empleado

	@receiver(post_save, sender = User)
	def crear_usuario_perfil(sender, instance, created, **kwargs):
		if created:
			Empleado.objects.create(empleado=instance)

	@receiver(post_save, sender=User)
	def guardar_usuario_perfil(sender, instance, **kwargs):
		instance.perfil.save()


class Cliente(models.Model):
	cod_cliente=models.AutoField(primary_key=True)
	"""
	el autofield es para poner un nombre personalizado
	a una id generada automaticamente
	y no usar la que provee django por defecto (id)
	"""
	nom_cliente=models.CharField(max_length=40)
	dir_cliente=models.CharField(max_length=100)
	tel_cliente=models.BigIntegerField()


class Pedido(models.Model):
	cod_pedido=models.IntegerField(primary_key=True)
	fec_pedido=models.DateTimeField()
	objects = models.Manager()

	def __str__(self):
		return self.cod_pedido

class Detalle_Pedido(models.Model):
	corr_det_ped=models.AutoField(primary_key=True)
	pizza=models.ForeignKey(Pizza,on_delete=models.CASCADE)
	pedido=models.ForeignKey(Pedido,on_delete=models.CASCADE)		
	cant_pedido=models.IntegerField()
#nuevos
class Registro(models.Model):
	cod_registro=models.AutoField(primary_key=True)
	cod_empleado=models.ForeignKey(Empleado, on_delete=models.CASCADE)
	cod_pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
	cod_cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
