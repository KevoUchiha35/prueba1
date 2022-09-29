from django.shortcuts import render, redirect
from .models import *
from .models import jugadores
from .forms import UserRegisterForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


#django nos permite tener forms#


# Create your views here.
# el context es para pedir datos a base

def feed(request):

  return render(request, 'social/feed.html')


def perfil(request):

  return render(request, 'social/perfil.html')


def registro(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('feed')
	else:
		form = UserRegisterForm()

	context = {'form': form}
	return render(request, 'social/registro.html', context)


def login(request):

  return render(request, 'social/login.html')


@login_required
def retorno(request):

  return render(request, 'social/prueba.html')


def formulario(request):
  if request.method == 'POST':  
       
        dato = jugadores.objects.create(
          
                user_id=request.POST['Usuario'], 
                nombre=request.POST['Nombre'], 
                apellido=request.POST['Apellidos'], 
                nickname=request.POST['Nickname'], 
                nacimiento=request.POST['Nacimiento'], 
                correo=request.POST['Correo'], 
                redsocial=request.POST['RedSocial'],  
                videojuegofav=request.POST['Videojuegofav'], 
                
				
               
            
          )
        dato.save()
  return render(request, 'social/datos.html')


