from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import Area,Cargo,Servicio
from apps.solicitudes.models import Paciente
from .forms import RegistrarPacienteForm,RegistrarAreaForm,RegistrarCargoForm,RegistrarServicioForm
from django.shortcuts import render_to_response
from django.core import serializers
from django.http import HttpResponse, Http404

import json
class PacienteBView(TemplateView):
	template_name = 'logistica/pacienteB.html'
	

def BuscarArea(request):		
	if request.is_ajax():			
		texto= request.GET['texto']
		seleccion = request.GET['seleccion']
		if seleccion=="0":
			area = Area.objects.filter(area_nom__icontains=texto)
			data = serializers.serialize('json',area,
			fields={'area_nom','area_descripcion'})
			return HttpResponse(data, content_type='application/json')	
		elif seleccion=="1":
			area = Area.objects.filter(id=texto)
			data = serializers.serialize('json',area,
			fields={'area_nom','area_descripcion'})
			return HttpResponse(data, content_type='application/json')		
	else :
		print "mal"
		raise Http404


def CreateArea(request):	
	if request.method == 'POST':
		form = RegistrarAreaForm(request.POST)
		response_data = {} 
		if form.is_valid():
			area= Area()
			area.area_nom = form.cleaned_data.get('area_nom')			
			area.area_descripcion = form.cleaned_data.get('area_descripcion')			
			area.save()		
			response_data['result'] = "La Nueva Area fue Registrada con Exito"
			#response_data['postpk'] = paciente.pk	        print "XXSS"
			#paciente.pac_fecnac = form.cleaned_data.get('DNI')	        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			data = json.dumps({'errors': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
			return HttpResponse(data,content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")	


def ModiArea(request):	
	if request.method == 'POST':		
		form = RegistrarAreaForm(request.POST)
		response_data = {} 
		if form.is_valid():
			area= Area.objects.get(id=form.cleaned_data.get('id'))
			area.area_nom = form.cleaned_data.get('area_nom')			
			area.area_descripcion = form.cleaned_data.get('area_descripcion')			
			area.save()	
			response_data['result'] = "Los datos del Area fueron Actualizados con Exito"				        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			data = json.dumps({'errors': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
			return HttpResponse(data,content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")


def BuscarServicio(request):		
	if request.is_ajax():			
		texto= request.GET['texto']
		seleccion = request.GET['seleccion']
		if seleccion=="0":
			consulta = Servicio.objects.select_related().filter(servi_nom__icontains=texto)
			lista=[]
			for servicio in consulta:
				d={'pk':servicio.id,'servicio': servicio.servi_nom,'descripcion': servicio.servi_descripcion
				,'costo': float(servicio.servi_costo),'tiempo':servicio.tiempo_requerido,'fk':servicio.area.id,'Area':servicio.area.area_nom}
				lista.append(d)
			#busqueda= Servicio.objects.select_related().filter(area__area_nom__contains="")		
			return HttpResponse(json.dumps(lista), content_type='application/json')	
		elif seleccion=="1":
			consulta = Servicio.objects.select_related().filter(area__area_nom__icontains=texto)
			lista=[]
			for servicio in consulta:
				d={'pk':servicio.id,'servicio': servicio.servi_nom,'descripcion': servicio.servi_descripcion
				,'costo': float(servicio.servi_costo),'tiempo':servicio.tiempo_requerido,'fk':servicio.area.id,'Area':servicio.area.area_nom}
				lista.append(d)
			return HttpResponse(json.dumps(lista), content_type='application/json')
		elif seleccion=="2":
			consulta = Servicio.objects.select_related().filter(id=texto)
			lista=[]
			for servicio in consulta:
				d={'pk':servicio.id,'servicio': servicio.servi_nom,'descripcion': servicio.servi_descripcion
				,'costo': float(servicio.servi_costo),'tiempo':servicio.tiempo_requerido,'fk':servicio.area.id,
				'Area':servicio.area.area_nom,'id_area':servicio.area.id}
				lista.append(d)
			return HttpResponse(json.dumps(lista), content_type='application/json')		
		elif seleccion=="5":
			servicio = Servicio.objects.filter(area__id=texto)
			data = serializers.serialize('json',servicio,fields={'servi_nom',})
			return HttpResponse(data, content_type='application/json')	
	else :
		print "mal"
		raise Http404


def CreateServicio(request):	
	if request.method == 'POST':
		form = RegistrarServicioForm(request.POST)
		response_data = {} 
		if form.is_valid():
			servicio= Servicio()
			servicio.servi_nom = form.cleaned_data.get('servi_nom')
			servicio.servi_descripcion = form.cleaned_data.get('servi_descripcion')	
			servicio.servi_costo = form.cleaned_data.get('servi_costo')
			servicio.tiempo_requerido = form.cleaned_data.get('tiempo_requerido')
			servicio.area = form.cleaned_data.get('area')
			servicio.save()
			response_data['result'] = "El nuevo Servicio fue Registrado con Exito"
			#response_data['postpk'] = paciente.pk	        print "XXSS"
			#paciente.pac_fecnac = form.cleaned_data.get('DNI')	        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			data = json.dumps({'errors': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
			return HttpResponse(data,content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")	


def ModiServicio(request):	
	if request.method == 'POST':		
		form = RegistrarServicioForm(request.POST)
		response_data = {} 
		if form.is_valid():
			servicio= Servicio.objects.get(id=form.cleaned_data.get('id'))
			servicio.servi_nom = form.cleaned_data.get('servi_nom')
			servicio.servi_descripcion = form.cleaned_data.get('servi_descripcion')	
			servicio.servi_costo = form.cleaned_data.get('servi_costo')
			servicio.tiempo_requerido = form.cleaned_data.get('tiempo_requerido')
			servicio.area = form.cleaned_data.get('area')
			servicio.save()	
			response_data['result'] = "Los datos del Servicio fueron Actualizados con Exito"				        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			data = json.dumps({'errors': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
			return HttpResponse(data,content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")



def BuscarCargo(request):		
	if request.is_ajax():			
		texto= request.GET['texto']
		seleccion = request.GET['seleccion']
		if seleccion=="0":
			cargo = Cargo.objects.filter(cargo_nom__icontains=texto)
			data = serializers.serialize('json',cargo,
			fields={'cargo_nom','cargo_descripcion'})
			return HttpResponse(data, content_type='application/json')	
		elif seleccion=="1":
			cargo = Cargo.objects.filter(id=texto)
			data = serializers.serialize('json',cargo,
			fields={'cargo_nom','cargo_descripcion'})
			return HttpResponse(data, content_type='application/json')		
	else :
		print "mal"
		raise Http404


def CreateCargo(request):	
	if request.method == 'POST':
		form = RegistrarCargoForm(request.POST)
		response_data = {} 
		if form.is_valid():
			cargo= Cargo()
			cargo.cargo_nom = form.cleaned_data.get('cargo_nom')			
			cargo.cargo_descripcion = form.cleaned_data.get('cargo_descripcion')			
			cargo.save()		
			response_data['result'] = "El Nuevo Cargo fue Registrado con Exito"
			#response_data['postpk'] = paciente.pk	        print "XXSS"
			#paciente.pac_fecnac = form.cleaned_data.get('DNI')	        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			data = json.dumps({'errors': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
			return HttpResponse(data,content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")	


def ModiCargo(request):	
	if request.method == 'POST':		
		form = RegistrarCargoForm(request.POST)
		response_data = {} 
		if form.is_valid():
			cargo= Cargo.objects.get(id=form.cleaned_data.get('id'))
			cargo.cargo_nom = form.cleaned_data.get('cargo_nom')			
			cargo.cargo_descripcion = form.cleaned_data.get('cargo_descripcion')			
			cargo.save()	
			response_data['result'] = "Los datos del Cargo fueron Actualizados con Exito"				        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			data = json.dumps({'errors': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
			return HttpResponse(data,content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")

# Create your views here.
def BuscarAjax(request):		
	if request.is_ajax():			
		texto= request.GET['texto']
		seleccion = request.GET['seleccion']
		if seleccion=="0":
			paciente = Paciente.objects.filter(DNI__icontains=texto)
			data = serializers.serialize('json',paciente,
			fields={'pac_nombre','pac_apellido','pac_telefono',
			'pac_direccion','DNI','pac_fecnac'})
			return HttpResponse(data, content_type='application/json')
		elif seleccion=="1":
			paciente = Paciente.objects.filter(pac_nombre__icontains=texto)
			data = serializers.serialize('json',paciente,
			fields={'pac_nombre','pac_apellido','pac_telefono',
			'pac_direccion','DNI','pac_fecnac'})
			return HttpResponse(data, content_type='application/json')
		elif seleccion=="2":
			paciente = Paciente.objects.filter(pac_nombre__icontains=texto)
			data = serializers.serialize('json',paciente,
			fields={'pac_nombre','pac_apellido','pac_telefono',
			'pac_direccion','DNI','pac_fecnac'})
			return HttpResponse(data, content_type='application/json')
		else :
			paciente = Paciente.objects.filter(id=texto)
			data = serializers.serialize('json',paciente,
			fields={'pac_nombre','pac_apellido','pac_telefono',
			'pac_direccion','DNI','pac_fecnac','pac_sexo','pac_obs'})
			return HttpResponse(data, content_type='application/json')		
	else :
		print "mal"
		raise Http404


def CreatePost(request):	
	if request.method == 'POST':
		form = RegistrarPacienteForm(request.POST)
		response_data = {} 
		if form.is_valid():
			paciente= Paciente()
			paciente.pac_nombre = form.cleaned_data.get('pac_nombre')
			paciente.pac_apellido = form.cleaned_data.get('pac_apellido')
			paciente.DNI = int(form.cleaned_data.get('DNI'))
			paciente.pac_direccion = form.cleaned_data.get('pac_direccion')
			paciente.pac_telefono = form.cleaned_data.get('pac_telefono')
			paciente.pac_sexo = form.cleaned_data.get('pac_sexo')
			paciente.pac_obs = form.cleaned_data.get('pac_obs')
			paciente.pac_fecnac = form.cleaned_data.get('pac_fecnac')
			paciente.save()
			response_data['result'] = "Los datos del Paciente fueron almacenados con Exito"
			#response_data['postpk'] = paciente.pk	        print "XXSS"
			#paciente.pac_fecnac = form.cleaned_data.get('DNI')	        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			data = json.dumps({'errors': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
			return HttpResponse(data,content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")


def home(req):
	tmpl_vars = {
		'form': RegistrarPacienteForm()
	}
	return render(req, 'logistica/pacienteB.html', tmpl_vars)


def HomeArea(req):
	tmpl_vars = {
		'form': RegistrarAreaForm()
	}
	return render(req, 'logistica/logisticaA.html', tmpl_vars)


def HomeCargo(req):
	tmpl_vars = {
		'form': RegistrarCargoForm()
	}
	return render(req, 'logistica/logisticaCargo.html', tmpl_vars)


def HomeServicio(req):
	tmpl_vars = {
		'form': RegistrarServicioForm()
	}
	return render(req, 'logistica/logisticaServicio.html', tmpl_vars)


def ModiPost(request):	
	if request.method == 'POST':
		instance = Paciente.objects.get(id=request.POST['id'])
		form = RegistrarPacienteForm(request.POST or None, instance=instance)
		response_data = {} 
		#print request.POST['id']
		if form.is_valid():
			paciente= Paciente.objects.get(id=form.cleaned_data.get('id'))
			paciente.pac_nombre = form.cleaned_data.get('pac_nombre')
			paciente.pac_apellido = form.cleaned_data.get('pac_apellido')
			paciente.pac_fecnac = form.cleaned_data.get('pac_fecnac')
			paciente.DNI = form.cleaned_data.get('DNI')            
			paciente.pac_direccion = form.cleaned_data.get('pac_direccion')
			paciente.pac_telefono = form.cleaned_data.get('pac_telefono')
			paciente.pac_sexo = form.cleaned_data.get('pac_sexo')
			paciente.pac_obs = form.cleaned_data.get('pac_obs')
			paciente.save()	
			response_data['result'] = "Los datos del Paciente fueron Modificados con Exito"
			#response_data['postpk'] = paciente.pk
			#response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')	        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			data = json.dumps({'errors': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
			return HttpResponse(data,content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")


def HomeModelo(req):
	tmpl_vars = {
		'form': RegistrarModeloForm()
	}
	return render(req, 'logistica/Modelo.html', tmpl_vars)




def BuscarModelo(request):		
	if request.is_ajax():			
		texto= request.GET['texto']
		seleccion = request.GET['seleccion']
		if seleccion=="0":
			servicio = Servicio.objects.filter(servi_nom__icontains=texto)
			data = serializers.serialize('json',servicio,
			fields={'servi_nom','servi_descripcion','servi_costo','area','tiempo_requerido'})
			return HttpResponse(data, content_type='application/json')	
		elif seleccion=="1":
			servicio = Servicio.objects.filter(id=texto)
			data = serializers.serialize('json',servicio,
			fields={'servi_nom','servi_descripcion','servi_costo','area','tiempo_requerido'})
			return HttpResponse(data, content_type='application/json')
		elif seleccion=="2":
			servicio = Servicio.objects.filter(id=texto)
			data = serializers.serialize('json',servicio,
			fields={'servi_nom','servi_descripcion','servi_costo','area','tiempo_requerido'})
			return HttpResponse(data, content_type='application/json')		
	else :
		print "mal"
		raise Http404


def CreateModelo(request):	
	if request.method == 'POST':
		form = RegistrarAreaForm(request.POST)
		response_data = {} 
		if form.is_valid():
			area= Area()
			area.area_nom = form.cleaned_data.get('area_nom')			
			area.area_descripcion = form.cleaned_data.get('area_descripcion')			
			area.save()		
			response_data['result'] = "La Nueva Area fue Registrada con Exito"
			#response_data['postpk'] = paciente.pk	        print "XXSS"
			#paciente.pac_fecnac = form.cleaned_data.get('DNI')	        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			data = json.dumps({'errors': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
			return HttpResponse(data,content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")	


def ModiModelo(request):	
	if request.method == 'POST':		
		form = RegistrarAreaForm(request.POST)
		response_data = {} 
		if form.is_valid():
			area= Area.objects.get(id=form.cleaned_data.get('id'))
			area.area_nom = form.cleaned_data.get('area_nom')			
			area.area_descripcion = form.cleaned_data.get('area_descripcion')			
			area.save()	
			response_data['result'] = "Los datos del Area fueron Actualizados con Exito"				        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			data = json.dumps({'errors': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
			return HttpResponse(data,content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")


