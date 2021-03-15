from django.urls import path
from . import views

urlpatterns= [
    path('', views.home, name='home'),
    path('us', views.us, name='us'),
    path('servicios', views.servicios, name='servicios'),
    path('productos', views.productos, name='productos'),
    path('contactos', views.contactos, name='contactos'),
]