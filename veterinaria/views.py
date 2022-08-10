from django.shortcuts import render, HttpResponse
from .models import Producto

def home(request):
    return render(request, 'home.html')

def contacto(request):
    return render(request, "contacto.html")

def services(request):
    return render(request, "services.html")

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})
def sesion(request):
    return render(request, "sesion.html")

def produc(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})