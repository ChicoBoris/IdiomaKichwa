from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Palabra
from django.urls import reverse

def home(request):
    return render(request, "home.html")

# Listado de palabras
def listadoPalabras(request):
    palabrasBdd = Palabra.objects.all()
    return render(request, "listadoPalabras.html", {'palabras': palabrasBdd})

# Eliminar una palabra
def eliminarPalabra(request, id):
    palabraEliminar = Palabra.objects.get(id=id)
    palabraEliminar.delete()
    # Mensajes de confirmación para sweetalert
    messages.success(request, "PALABRA ELIMINADA EXITOSAMENTE.")
    return redirect('listadoPalabras')

# Formulario para nueva palabra
def nuevaPalabra(request):
    return render(request, 'nuevaPalabra.html')

# Guardar una nueva palabra
def guardarPalabra(request):
    quechua = request.POST["quechua"]
    espanol = request.POST["espanol"]
    descripcion = request.POST.get("descripcion", '') # default empty string
    nuevaPalabra = Palabra.objects.create(quechua=quechua, espanol=espanol, descripcion=descripcion)
    # Mensajes de confirmación para sweetalert
    messages.success(request, "PALABRA GUARDADA EXITOSAMENTE.")
    return redirect('listadoPalabras')

# Editar una palabra existente
def editarPalabra(request, id):
    palabraEditar = Palabra.objects.get(id=id)
    return render(request, 'editarPalabra.html', {'palabraEditar': palabraEditar})
