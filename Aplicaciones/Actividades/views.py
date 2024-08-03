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