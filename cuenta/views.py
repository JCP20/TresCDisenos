from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
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
#condicional usado para verificar de que forma se accede a la pagina
#si se entra desde el metodo get no hara nada, solo se accede a la pagina
    if request.method == 'GET':
        return render(request,'Login.html')
#si se entra desde post significa que se introdujeron datos para iniciar sesion
#por lo tanto se pasa a procesarlos
    else:
        user = authenticate(request, username = request.POST["username"], password = request.POST["contraseña"])        
        if user == None:
            return render(request,'Login.html', {
                'error' : "Correo electronico o contaseña incorrecta"
            })
        else:
            auth_login(request, user)
            return render(request,'bolsa.html')

def registro(request):
    return render(request,'Registro.html')
def tienda(request):
    return render(request,'tienda.html')