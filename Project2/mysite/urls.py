from django.urls import path
from django.contrib import admin
from . import views


apps_name = 'mysite'

urlpatterns = [

    path('', views.index, name='index'),

    path('Register', views.Register, name='Register'),

    path('login', views.login, name='login'),

    path('contact', views.contact, name='contact'),


]
