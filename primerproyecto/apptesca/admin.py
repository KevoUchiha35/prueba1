from django.contrib import admin
from .models import Noticias

# Register your models here.

class NoticiaAdmin(admin.ModelAdmin):

    readonly_fields=("created","update")


admin.site.register(Noticias, NoticiaAdmin)

