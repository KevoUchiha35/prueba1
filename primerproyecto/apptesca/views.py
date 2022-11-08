from django.shortcuts import render, redirect
from .models import *
from .models import jugadores
from .models import contactanos
from .models import tienda
from .models import Imagenes
from .forms import UserRegisterForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail


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
            plataforma_xbox=request.POST['plataforma_xbox'],





        )
        dato.save()
    return render(request, 'social/datos.html')


def consulta(request):
    info = jugadores.objects.all()

    context = {'posts': info}

    return render(request, 'social/consultas.html', context)


def carusel(request):
    return render(request, 'social/carrusel.html')


def correo(request):
    if request.method == 'POST':
        correoPru = request.POST['correo']
        mensaje = request.POST['nombre'] + ' ' + request.POST['apellidos'] + ', ' + \
            request.POST['nickname'] + ' ' + \
            request.POST['correo'] + ' ' + request.POST['asunto']
        correito = contactanos.objects.create(

            nombre=request.POST['nombre'],
            apellido=request.POST['apellidos'],
            nickname=request.POST['nickname'],
            email=request.POST['correo'],
            asunto=request.POST['asunto'],
        )
        correito.save()
        send_mail(
            'Correo de Confirmacion',
            mensaje,
            'bienvenido a los akatsuki',
            [correoPru, 'kevouchiha35@gmail.com'],
            fail_silently=False
        )
    context = {}
    return render(request, 'social/correo.html')


def principal(request):
    return render(request, 'social/inicio.html')


def compras(request):
    print(request)
    if request.method == 'POST':
        dato = tienda.objects.create(
            user_id=request.POST['user'],
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            correo=request.POST['correo'],
            numero=request.POST['Numero'],
            pago=request.POST['metodo_pago'],
            total=request.POST['total'])
        dato.save()
    return render(request, 'social/carrito.html')


def carro(request):
    info = tienda.objects.all()

    context = {'posts': info}

    return render(request, 'social/consultas_carrito.html', context)


def home(request):
 noticias=Imagenes.objects.all()
  
 return render(request, 'social/inicio.html', {"noticias":noticias})
