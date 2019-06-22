"""pizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('pizza/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('index/', include('pi.urls')),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url('accounts/login/', TemplateView.as_view(template_name='login.html'), name='login'),
    url(r'^accounts/logout/$', TemplateView.as_view(template_name='logged_out.html'), name='logout'),
    url(r'^accounts/password_change/$', include('django.contrib.auth.urls'), name='password_change'),
    url(r'^accounts/password_change/done/$', include('django.contrib.auth.urls'), name='password_change_done'),
    url(r'^accounts/password_reset/$', TemplateView.as_view(template_name='password_resert_form.html'),
        name='password_reset'),
    url(r'^accounts/password_reset/done/$', include('django.contrib.auth.urls'), name='password_reset_done'),
    url(r'^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        include('django.contrib.auth.urls'), name='password_reset_confirm'),
    url(r'^accounts/reset/done/$', include('django.contrib.auth.urls'), name='password_reset_complete'),
]