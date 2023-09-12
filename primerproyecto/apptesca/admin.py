from django.contrib import admin
from .models import Noticias, contactanos, Producto, tienda
# Register your models here.

class NoticiaAdmin(admin.ModelAdmin):

    readonly_fields=("created","update")



class ContactanosAdmin(admin.ModelAdmin):
    list_display=("nombre","apellido")
    readonly_fields=()


class ProductoAdmin(admin.ModelAdmin):

    readonly_fields=()

class TiendaAdmin(admin.ModelAdmin):

    readonly_fields=()


admin.site.register(Noticias, NoticiaAdmin)
admin.site.register(contactanos, ContactanosAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(tienda, TiendaAdmin)