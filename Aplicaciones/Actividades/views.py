# views.py
from django.shortcuts import redirect,render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def home (request):
    return render(request,'home.html')

def exit(request):
    logout(request)
    return redirect('actividades')



@login_required
def actividades(request):
    return render(request, 'actividades.html')

def aprender(request):
    return render(request, 'aprender.html')

def sonido(request):
    return render(request, 'sonido.html')

def palabra(request):
    return render(request, 'palabra.html')
