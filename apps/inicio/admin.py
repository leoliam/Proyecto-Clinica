from django.contrib import admin
from .models import *

class PromocionAdmin(admin.ModelAdmin):
	list_display=('titulo','cargo_descripcion','imagen')

admin.site.register(Promocion,PromocionAdmin)

