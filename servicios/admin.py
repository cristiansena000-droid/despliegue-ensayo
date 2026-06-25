from django.contrib import admin
from .models import Servicio
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('creado','actualizado')

admin.site.register(Servicio,ServicioAdmin),


