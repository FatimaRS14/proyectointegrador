from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'home.html')

def contacto(request):
    return render(request, "contacto.html")

def services(request):
    return render(request, "services.html")

def productos(request):
    return render(request, "productos.html")

def sesion(request):
    return render(request, "sesion.html")

