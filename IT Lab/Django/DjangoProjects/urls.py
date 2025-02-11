"""
URL configuration for DjangoProjects project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include,path
# from app import forms, views
# from TwoSum import views
# from Webform import views
# from Empform import views
# from Calculator import views
# from Magazine import views
# from Book import views
# from FormTransfer import views


urlpatterns = [
    path('',include('Webform.urls')),
    path('Empform/',include('Empform.urls')),
    path('Calculator/',include('Calculator.urls')),
    path('Magazine/',include('Magazine.urls')),
    path('Book/',include('Book.urls')),
    path('Form/',include('FormTransfer.urls')),
    path('Transfer/',include("TransferBack.urls"))
]
