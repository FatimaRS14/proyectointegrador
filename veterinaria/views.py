from django.shortcuts import render, HttpResponse
from .models import Producto, Servicio

def home(request):
    return render(request, 'home.html')

def contacto(request):
    return render(request, "contacto.html")

def services(request):
     services = Servicio.objects.all()
     return render(request, 'services.html', {'services': services})

    

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def sesion(request):
    return render(request, "sesion.html")

def registro(request):
    return render(request, "registro.html")


