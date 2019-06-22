from django.db import models

# Create your models here

class Ingrediente(models.Model):
    ingrediente_id = models.IntegerField(primary_key=True)
    nom_ingrediente = models.CharField(max_length=25)

    def __str__(self):
        return self.nom_ingrediente


class Pizza(models.Model):
    pizza_id = models.IntegerField(primary_key=True)
    nom_pizza = models.CharField(max_length=30)

    objects = models.Manager()

    def __str__(self):
        return self.nom_pizza

class TipoMasas(models.Model):
    tipo_Masa_Id = models.IntegerField(primary_key=True)
    nom_tipo = models.CharField(max_length=7)

    def __str__(self):
        return self.nom_tipo

class Hecha_De(models.Model):
    corr_hec_de = models.AutoField(primary_key=True)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    tipomasa = models.ForeignKey(TipoMasas, on_delete=models.CASCADE)

    def __str__(self):
        return
        pass

class Empleado(models.Model):
    cod_empleado = models.IntegerField(primary_key=True)
    nom_empleado = models.CharField(max_length=40)
    pass_empleado = models.CharField(max_length=20, blank=False)

    objects = models.Manager()

    def __str__(self):
        return self.nom_empleado

class Cliente(models.Model):
    cod_cliente = models.IntegerField(primary_key=True)
    nom_cliente = models.CharField(max_length=40)
    dir_cliente = models.CharField(max_length=100)
    tel_cliente = models.BigIntegerField()

class Pedido(models.Model):
    cod_pedido = models.IntegerField(primary_key=True)
    fec_pedido = models.DateTimeField()

class Detalle_Pedido(models.Model):
    corr_det_ped = models.AutoField(primary_key=True)
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    cant_pedido = models.IntegerField()


class Registro(models.Model):
    cod_registro = models.AutoField(primary_key=True)
    cod_empleado = models.ForeignKey(Empleado,on_delete=models.CASCADE)
    cod_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cod_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
