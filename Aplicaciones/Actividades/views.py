# views.py
from django.shortcuts import render,redirect

def home(request):
    return render(request, 'actividades/plantilla.html')
