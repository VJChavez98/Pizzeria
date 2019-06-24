from django.urls import path
from . import views

#django login, del in case of err
from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.urls import include, reverse


app_name = 'pi'

urlpatterns=[
    path('', views.IndexView.as_view()),
    path('index/', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/',views.HomeView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('consultar/', views.ConsultarPedido.as_view(), name='detailPedido'),

]