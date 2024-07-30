from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),  # Home page
    path('actividades', views.actividades, name='actividades')
]
