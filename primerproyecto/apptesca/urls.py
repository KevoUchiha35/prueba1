from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings

from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

# Construir la URL completa de un archivo multimedia




urlpatterns = [
    path('', views.principal, name='inicio'),
    url('^perfil/$' , views.perfil, name="perfil"),
    url('^register/$' , views.registro, name="registro"),
    url('^login/$' , LoginView.as_view(template_name='social/login.html'), name="login"),
    url('^logout/$' , LogoutView.as_view(template_name='social/logout.html'), name="logout"),
    url('^acceso/$' , views.retorno, name="prueba"),
    url('^datos/$' , views.formulario, name="datos"),
    url('^consultas/$' , views.consulta, name="consultas"),
    url('^carrusel/$' , views.carusel, name="carrusel"),
    url('^correo/$' , views.correo, name="correo"),
    url('^feed/$' , views.feed, name="feed"),
    url('^carrito/' , views.compras, name="carrito"),
    url('^consultas_carrito/$' , views.carro, name="consultas_carrito"),
    url('^noticias/$' , views.home, name="noticias"),
    url('^publicacion/$' , views.ppost, name="publicacion"),
    url('^menu/$' , views.agregar, name="menu"),
    url('^productoss/$' , views.gamer, name="productoss"),
    url('^registros/$' , views.llenar, name="registros"),
    url('^registrar_tienda/$' , views.campos, name="registrar_tienda"),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)