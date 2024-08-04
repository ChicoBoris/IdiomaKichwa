from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página de inicio
    path('listadoPalabras/', views.listadoPalabras, name='listadoPalabras'),  # Listar todas las palabras
    path('eliminarPalabra/<int:id>', views.eliminarPalabra, name='eliminarPalabra'),  # Eliminar una palabra por id
    path('nuevaPalabra/', views.nuevaPalabra, name='nuevaPalabra'),  # Formulario para nueva palabra
    path('guardarPalabra/', views.guardarPalabra, name='guardarPalabra'),  # Guardar una nueva palabra
    path('editarPalabra/<int:id>', views.editarPalabra, name='editarPalabra'),  # Editar una palabra existente por id
]
