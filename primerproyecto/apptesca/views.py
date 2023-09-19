from django.shortcuts import render, redirect
from .models import *
from .models import jugadores
from .models import contactanos
from .models import tienda
from .models import Noticias
from .models import Producto
from .forms import UserRegisterForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, Page
user = ""
#django nos permite tener forms#


# Create your views here.
# el context es para pedir datos a base

def feed(request):

    arroba = jugadores.objects.all()

    return render(request, 'social/feed.html', {'arroba':arroba})


def perfil(request):

    per = jugadores.objects.all()

    if request.method == 'POST':
        imagen_profile = request.FILES['imagen_profile']  # Usa request.FILES para acceder al archivo
        # Configura un sistema de almacenamiento para las imágenes
        pro = FileSystemStorage(location='media/productos')
        filename = pro.save(imagen_profile.name, imagen_profile)  # Guarda la imagen en el sistema de almacenamiento
        print(filename)
        imagen_url = ("productos/"+filename)  # Obtiene la URL de la imagen
        print(imagen_url)
        dato = jugadores.objects.create(
            imagen_profile=imagen_url  # Guarda la URL de la imagen en la base de datos
        )
        dato.save()
        global user
        print (user)
        messages.success(request,"tu usuario es:"+ user)   
        return render(request, 'social/perfil.html', {'per':per})

    return render(request, 'social/perfil.html', {'per': per})




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
    global usuarios
    usuarios = registro.objects.get()
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
            numero=request.POST['Numero'],
            direccion=request.POST['Direccion'],
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


@login_required




def compras(request):
    ejemplos = Producto.objects.all()

    # Configura el paginador con los ejemplos y la cantidad de ejemplos por página
    paginator = Paginator(ejemplos, 6)  # Cambia 6 al número deseado de ejemplos por página

    # Obten la página actual del GET request, si no se especifica, será la página 1
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    if request.method == 'POST':
        dato = tienda.objects.create(
            user_id=request.POST['user'],
            pago=request.POST['metodo_pago'],
            total=request.POST['total']
        )
        dato.save()

    return render(request, 'social/carrito.html', {'page': page})




def carro(request):
    info = jugadores.objects.all()
    ejemplo = tienda.objects.all()
    

    return render(request, 'social/consultas_carrito.html', {'info' :info , 'ejemplo' :ejemplo})


def home(request):
    noticias = Noticias.objects.all()
    context = {'noticias':noticias}
    return render(request, 'social/post.html', context)

def ppost(request):

    return render(request, 'social/post.html')

def agregar(request):

    
        return render(request, 'social/menu_admin.html')

def gamer(request):
    ejemplos = Producto.objects.all()
    if request.method == 'POST':
        nombre = request.POST['Nombre']
        precio = request.POST['Precio']
        descripcion = request.POST['Descripcion']
        imagen = request.FILES['Imagen']  # Usa request.FILES para acceder al archivo

        # Configura un sistema de almacenamiento para las imágenes
        fs = FileSystemStorage(location='media/productos')
        filename = fs.save(imagen.name, imagen)  # Guarda la imagen en el sistema de almacenamiento
        print(filename)
        imagen_url = ("productos/"+filename)  # Obtiene la URL de la imagen
        print(imagen_url)
        dato = Producto.objects.create(
            nombre=nombre,
            precio=precio,
            descripcion=descripcion,
            imagen=imagen_url  # Guarda la URL de la imagen en la base de datos
        )
        dato.save()

        return render(request, 'social/menu_admin.html', {'ejemplos': ejemplos})

    return render(request, 'social/menu_admin.html', {'ejemplos': ejemplos})



