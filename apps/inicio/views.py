from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from apps.logistica.models import Servicio
from apps.inicio.models import Promocion
from django.core import serializers
from django.http import HttpResponse, Http404
from datetime import datetime
from datetime import date




class IndexView(TemplateView):
	template_name = 'inicio/index.html'

def cargar_servicio(request):
	consulta = Servicio.objects.select_related().filter(area__area_nom__icontains='Laboratorio')
	consulta2 = Servicio.objects.select_related().filter(area__area_nom__icontains='Ecografia')
	consulta3 = Servicio.objects.select_related().filter(area__area_nom__icontains='Medicina General')
	consulta4 = Servicio.objects.select_related().filter(area__area_nom__icontains='Ginecologia')
	consulta5 = Servicio.objects.select_related().filter(area__area_nom__icontains='Obstetricia')
	consulta6 = Promocion.objects.filter(fecha_registro__month=datetime.now().month)
	return render(request, 'inicio/principal.html',{'consulta':consulta, 'consulta2':consulta2,'consulta3':consulta3,'consulta4':consulta4,'consulta5':consulta5,'consulta6':consulta6})
		
