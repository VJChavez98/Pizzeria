from django.contrib import admin
from .models import Pizza, Ingrediente, TipoMasas, Hecha_De
from .models import Empleado, Cliente, Pedido, Detalle_Pedido, Registro
# Register your models here.

admin.site.register(Pizza)
admin.site.register(Ingrediente)
admin.site.register(TipoMasas)
admin.site.register(Hecha_De)
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Detalle_Pedido)
admin.site.register(Registro)
