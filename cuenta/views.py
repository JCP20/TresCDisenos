from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def galeria(request):
    return render(request,'galeria.html')
def cuenta(request):
    return render(request,'cuenta.html')
def infocuenta(request):
    return render(request,'detalles.html')
def bolsa(request):
    return render(request,'bolsa.html')
def login(request):
    return render(request,'Login.html')
def registro(request):
    return render(request,'Registro.html')
def tienda(request):
    return render(request,'tienda.html')