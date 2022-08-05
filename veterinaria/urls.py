from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contacto/', views.contacto, name="contacto"),
    path('services/', views.services, name="services"),
    path('productos/', views.productos, name="productos"),
    path('sesion/', views.sesion, name="sesion"),

]