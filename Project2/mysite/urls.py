from django.urls import path

from . import views

apps_name = 'mysite'

urlpatterns = [

    path('', views.index, name='index'),

    path('Register', views.Register, name='Register'),

    path('signin', views.signin, name='signin'),

    path('contact', views.contact, name='contact'),


]
