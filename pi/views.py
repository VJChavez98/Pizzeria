from django.shortcuts import render
from .models import *
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.

class IndexView(generic.ListView):
	template_name='index.html'
	context_object_name='pizza_list'

	def get_queryset(self):
		return Pizza.objects.all()

class HomeView(generic.DetailView):
	model=Pizza
	template_name='home.html'

#comentar en caso de err

class LoginView(generic.DetailView):
	model=Empleado
	template_name='registration/login.html'

#...

class ConsultarPedido(generic.ListView):
	model = Pedido
	template_name = 'pages/ConsultarPedido.html'
	context_object_name = 'detalle'



def detallePedido(request, cod_pedido):
	pedido = get_object_or_404(Pedido, pk=cod_pedido)
	return render(request, 'pages/Pedido_detalle.html', {'pedido': pedido})
#nuevo
def home(request, pizza_id):
	pizza=get_object_or_404(Pizza, pk=pizza_id)
	#return HttpResponse("estas mirando la pizza: %s." % pizza_id)
	return render(request,'home.html', {'pizza':pizza})


#comentar en caso de error
"""
def login(request, string):
	return render(request,'pi/login.html')
#......
"""