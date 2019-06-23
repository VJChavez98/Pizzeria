from django.urls import path, include, reverse
from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from . import views


app_name='pi'

urlpatterns = [
    path('', views.indexView.as_view()),
    path('index/', views.indexView.as_view(), name='index'),

    path('<int:pk>', views.pizzasView.as_view(), name='pizzas'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),





]
