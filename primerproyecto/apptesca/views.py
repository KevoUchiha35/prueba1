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
#django nos permite tener forms#


# Create your views here.
# el context es para pedir datos a base

def feed(request):

    arroba = jugadores.objects.all()

    return render(request, 'social/inicio.html', {'arroba':arroba})


def perfil(request):
    per = jugadores.objects.all()
    return render(request, 'social/perfil.html', {'per':per})


def actualiza(request):
    try:
        per = jugadores.objects.get(user=request.user)  # Obtén el objeto de jugador existente del usuario
    except jugadores.DoesNotExist:
        per = None

    if request.method == 'POST':
        if per:
        # Obtener los valores del formulario
            nuevo_nombre = request.POST.get('nombre', per.nombre)
            nuevo_apellido = request.POST.get('apellido', per.apellido)
            nuevo_correo = request.POST.get('correo', per.correo)
            nuevo_numero = request.POST.get('numero', per.numero)
            nuevo_direccion = request.POST.get('direccion', per.direccion)
            nuevo_videojuegofav = request.POST.get('videojuegofav', per.videojuegofav)

        # Verificar si los campos están en blanco y mantener los valores actuales si es así
            per.nombre = nuevo_nombre if nuevo_nombre.strip() else per.nombre
            per.apellido = nuevo_apellido if nuevo_apellido.strip() else per.apellido
            per.correo = nuevo_correo if nuevo_correo.strip() else per.correo
            per.numero = nuevo_numero if nuevo_numero.strip() else per.numero
            per.direccion = nuevo_direccion if nuevo_direccion.strip() else per.direccion
            per.videojuegofav = nuevo_videojuegofav if nuevo_videojuegofav.strip() else per.videojuegofav

        # Guardar los cambios en la base de datos
            per.save()
            # Verificar si se está actualizando la imagen de perfil
            if 'imagen_profile' in request.FILES:
                # Verifica si el jugador tiene una imagen de perfil existente y elimínala
                if per.imagen_profile:
                    fs = FileSystemStorage(location='media/productos')
                    fs.delete(per.imagen_profile.name)

                # Procede a guardar la nueva imagen de perfil
                imagen_profile = request.FILES['imagen_profile']
                pro = FileSystemStorage(location='media/productos')
                filename = pro.save(imagen_profile.name, imagen_profile)
                per.imagen_profile = 'productos/' + filename
                per.save()

            return redirect('perfil')  # Redirigir a la página de perfil

    return render(request, 'social/actualizar.html', {'per': per})


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


def formulario(request): #mandar el request 
    up = jugadores.objects.all()
    if request.method == 'POST':#solicitud de que se esta haciendo un post
        user_id = request.POST.get('Usuario')#se usa el get porque obtiene el dato de mi variable que esta en front y lo trae para guardarlo
        nombre = request.POST.get('Nombre')
        apellido = request.POST.get('Apellidos')
        nickname = request.POST.get('Nickname')
        nacimiento = request.POST.get('Nacimiento')
        correo = request.POST.get('Correo')
        numero = request.POST.get('Numero')
        direccion = request.POST.get('Direccion')
        redsocial = request.POST.get('RedSocial')
        videojuegofav = request.POST.get('Videojuegofav')
        plataforma_xbox = request.POST.get('Plataforma_xbox')  # Cambio de 'Plataforma_xbox' a 'plataforma_xbox'
        imagen_profile = request.FILES['imagen_profile']

        fs = FileSystemStorage(location='media/productos')
        filename = fs.save(imagen_profile.name, imagen_profile)  # Guarda la imagen en el sistema de almacenamiento
        print(filename)
        imagen_url = ("productos/"+filename)  # Obtiene la URL de la imagen
        print(imagen_url)
        dato = jugadores.objects.create(
            user_id=user_id,
            nombre=nombre,
            apellido=apellido,
            nickname=nickname,
            nacimiento=nacimiento,
            correo=correo,
            numero=numero,
            direccion=direccion,
            redsocial=redsocial,
            videojuegofav=videojuegofav,
            plataforma_xbox=plataforma_xbox,
            imagen_profile=imagen_url  # Guarda la URL de la imagen en la base de datos
        )
        dato.save()
        if dato:
            print("logrado")

        return render(request, 'social/datos.html', {'up': up})
    return render(request, 'social/datos.html', {'up': up})

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
    ejemplos = Producto.objects.all()
    auto = jugadores.objects.filter()

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

    return render(request, 'social/carrito.html', {'page': page, 'auto': auto })

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

def buscar_producto(request):
    
    if 'q' in request.GET:
        query = request.GET['q']
        resultados = Producto.objects.filter(nombre__icontains=query)
    else:
        resultados = None

    return render(request, 'social/carrito.html', {'resultados': resultados})