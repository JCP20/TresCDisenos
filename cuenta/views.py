from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from .models import DireccionEnvio
from django.contrib.auth.forms import UserCreationForm
from .models import Artículo

# Create your views here.
def galeria(request):
    return render(request,'galeria.html')

def panel_usuario(request):
    try:
            print(request.POST)
            print("jacobo")
            dirrecionEnvio = DireccionEnvio(user = request.user, telefono = request.POST["telefono"], direccion = request.POST["direccion"], barrio = request.POST['barrio'], observaciones = request.POST['observaciones'])
            dirrecionEnvio.save()
            return render(request,'panel_usuario.html', {'msg': 'Direccion de envio guardado correctamente'})
    except :
            print
            return render(request,'panel_usuario.html', {'msg': 'No se pudo guardar'})        


def infoproducto(request):
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
            return redirect("panel_usuario")
            
def registro(request):
    # Si se ingresa desde el método GET sólo se accede a la página
    if request.method == 'GET':
        return render(request,'Registro.html',{'msg':""})
    else:
        # Si se ingresa desde el método POST se verifica que coincidan las contraseñas
        if request.POST.get('contraseña1') == request.POST.get('contraseña2'):
            try:
                print(request.POST)
                user = User.objects.create_user(username = request.POST["username"], password = request.POST["contraseña1"], email = request.POST["correo"], first_name = request.POST['nombre'].title(), last_name = request.POST['apellido'].title())
                user.save()
                return render(request,'Registro.html', {'msg': 'Registrado correctamente, puedes iniciar sesión.'})

            except :
                print
                return render(request,'Registro.html', {'msg': 'El nombre de usuario ya está en uso'})        
       
        else:
            return render(request,'Registro.html', {'msg': 'Las contraseñas no coinciden'})        

def tienda(request):
    context ={
       'items' : Artículo.objects.all()
    }
    return render(request,"tienda.html",context)

def bolsa(request):
    context ={
       'items' : Artículo.objects.all()
    }
    return render(request,"bolsa.html",context)