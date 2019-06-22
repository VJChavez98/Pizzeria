from django.views import generic
from django.urls import reverse
from .models import Pizza, Empleado
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect


class indexView(generic.ListView):

    template_name = 'index.html'
    context_object_name = 'pizza_list'

    def get_queryset(self):
        return Pizza.objects.all()


    def login(self):
        template_name='login.html'
        return HttpResponseRedirect(reverse('login'))

class pizzasView(generic.DetailView):
    model = Pizza
    template_name = 'pizzas.html'

def pizzas(request, pizza_id):
    pizza = get_object_or_404(Pizza, pk=pizza_id)
    return render(request, 'pizzas.html', {'pizza': pizza})
