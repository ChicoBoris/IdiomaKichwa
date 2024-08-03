from django.urls import path
from . import views
from .views import  exit
urlpatterns = [
    path('home', views.home, name='home'),  # Home page
    path('actividades', views.actividades, name='actividades'),
    path('logout/', exit, name='exit'),
]
