from django.contrib import admin
from .models import Imagenes

# Register your models here.

class ImagenesAdmin(admin.ModelAdmin):

    readonly_fields=("created","update")


admin.site.register(Imagenes, ImagenesAdmin)

