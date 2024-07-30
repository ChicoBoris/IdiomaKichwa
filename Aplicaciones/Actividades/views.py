# views.py
from django.shortcuts import render

def home (request):
    return render(request,'home.html')

def actividades(request):
    return render(request, 'actividades.html')