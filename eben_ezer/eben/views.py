from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'eben/home.html')

def us(request):
    return render(request, 'eben/us.html')

def servicios(request):
    return render(request, 'eben/servicios.html')

def productos(request):
    return render(request, 'eben/productos.html')

def contactos(request):
    return render(request, 'eben/contactos.html')