from django.urls import path
from . import views
from .views import  exit
urlpatterns = [
    path('home', views.home, name='home'),  # Home page
    path('actividades', views.actividades, name='actividades'),
    path('actividades/aprender/', views.aprender, name='aprender'),
    path('aprender/', views.aprender, name='aprender'),
    path('sonido/', views.sonido, name='sonido'),
    path('palabra/', views.palabra, name='palabra'),
    path('logout/', exit, name='exit'),
]
