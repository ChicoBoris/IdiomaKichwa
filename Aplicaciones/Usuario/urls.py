# Aplicaciones/Usuario/urls.py
from django.urls import path
from .views import home, actividades  # Asegúrate de importar todas las vistas necesarias

urlpatterns = [
    path('', home, name='home'),  # Ruta para la página principal
    path('home/', home, name='home'),
    path('actividades/', actividades, name='actividades'),
]
