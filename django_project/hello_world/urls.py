from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello_world', views.hello_world, name='hello_world'),
    path('register', views.register, name='register'),
    path('registered', views.registered, name='registered'),
    path('all', views.listall, name='listall')
]