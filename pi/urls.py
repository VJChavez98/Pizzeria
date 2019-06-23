from django.urls import path
from . import views

#django login, del in case of err
from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.urls import include, reverse


app_name = 'pi'

urlpatterns=[
    #path(' ',views.index,name = 'index'),
    #esto es por defecto pi/
    path('', views.IndexView.as_view()),
    path('', views.IndexView.as_view(), name = 'index'),
    #login view. Commment
	#path('<slug:slug>/',views.LoginView.as_view(), name='login'),
	#path('login/',views.LoginView.as_view(), name='login'),

    #ejemplo: /pi/2
    path('<int:pk>/',views.HomeView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),

]