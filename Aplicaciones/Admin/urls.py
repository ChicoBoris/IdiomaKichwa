from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),  # Home page
    path('listadoPalabras/', views.listadoPalabras, name='listadoPalabras'),  # List all words
    path('eliminarPalabra/<int:id>', views.eliminarPalabra, name='eliminarPalabra'),  # Delete a word by id
    path('nuevaPalabra/', views.nuevaPalabra, name='nuevaPalabra'),  # Form for new word
    path('guardarPalabra/', views.guardarPalabra, name='guardarPalabra'),  # Save a new word
    path('editarPalabra/<int:id>', views.editarPalabra, name='editarPalabra'),  # Edit an existing word by id
]
