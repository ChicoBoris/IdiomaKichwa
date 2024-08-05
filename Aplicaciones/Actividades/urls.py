from django.urls import path
from . import views
from .views import  exit
urlpatterns = [
    path('home', views.home, name='home'),  # Home page
    path('actividades', views.actividades, name='actividades'),
    path('aprender/', views.aprender, name='aprender'),
    path('sonido/', views.sonido, name='sonido'),
    path('logout/', exit, name='exit'),
]
