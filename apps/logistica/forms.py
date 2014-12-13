from django import forms
from .models import Area,Cargo,Servicio,Modelo
from apps.solicitudes.models import Paciente
class RegistrarPacienteForm(forms.ModelForm):
	id = forms.IntegerField(required=False,widget = forms.HiddenInput(
		attrs={ 'id': 'codigo'}))
	pac_nombre = forms.CharField(widget= forms.TextInput(
		attrs={ 'class' : 'input-sm', 'id': 'nombres'}))
	pac_apellido = forms.CharField(widget= forms.TextInput(
		attrs={'class' : 'input-sm' , 'id': 'apellidos'}))
	DNI = forms.CharField(max_length=8,min_length=8,widget= forms.TextInput(
		attrs={'class' : 'input-xs' , 'id': 'dni'}))
	pac_direccion = forms.CharField(widget= forms.TextInput(
		attrs={'class' : 'input-xs' , 'id': 'direccion'}))
	pac_fecnac= forms.DateField(widget=forms.DateInput( 
		attrs={'id': 'fecnac'}))
	pac_telefono = forms.CharField(widget= forms.TextInput(
		attrs={'class' : 'input-xs'  , 'id': 'tel'}))	
	pac_sexo = forms.ChoiceField(required=False, choices=(('F', 'Femenino'),('M', 'Masculino')),
		widget= forms.Select(attrs={'class' : 'input-sm' ,'id': 'sex'}))
	pac_obs = forms.CharField(required=False,widget= forms.Textarea(
		attrs={'class' : 'custom-scroll' , 'id': 'observacion'}))	
	class Meta:
		model = Paciente


class RegistrarAreaForm(forms.ModelForm):
	id = forms.IntegerField(required=False,widget = forms.HiddenInput(
		attrs={ 'id': 'codigo'}))
	area_nom = forms.CharField(widget= forms.TextInput(
		attrs={ 'class' : 'input-sm', 'id': 'nombres'}))	
	area_descripcion = forms.CharField(required=False,widget= forms.Textarea(
		attrs={'class' : 'custom-scroll' , 'id': 'observacion'}))	
	class Meta:
		model = Area


class RegistrarCargoForm(forms.ModelForm):
	id = forms.IntegerField(required=False,widget = forms.HiddenInput(
		attrs={ 'id': 'codigo'}))
	cargo_nom = forms.CharField(widget= forms.TextInput(
		attrs={ 'class' : 'input-sm', 'id': 'nombres'}))	
	cargo_descripcion = forms.CharField(required=False,widget= forms.Textarea(
		attrs={'class' : 'custom-scroll' , 'id': 'observacion'}))	
	class Meta:
		model = Cargo


class RegistrarServicioForm(forms.ModelForm):
	id = forms.IntegerField(required=False,widget = forms.HiddenInput(
		attrs={ 'id': 'codigo'}))	
	servi_nom = forms.CharField(widget= forms.TextInput(
		attrs={ 'class' : 'input-sm', 'id': 'nombres'}))	
	servi_descripcion = forms.CharField(required=False,widget= forms.Textarea(
		attrs={'class' : 'custom-scroll' , 'id': 'observacion'}))
	servi_costo = forms.CharField(widget= forms.TextInput(
		attrs={'class' : 'input-xs' , 'id': 'costo','type': 'number'}))
	tiempo_requerido = forms.CharField(widget= forms.TextInput(
		attrs={'class' : 'input-xs' , 'id': 'TR','type': 'number'}))
	class Meta:
		model = Servicio


class RegistrarModeloForm(forms.ModelForm):
	id = forms.IntegerField(required=False,widget = forms.HiddenInput(
		attrs={ 'id': 'codigo'}))
	Nombre = forms.CharField(widget= forms.TextInput(
		attrs={ 'class' : 'input-sm', 'id': 'nombres'}))	
	descripcion = forms.CharField(required=False,widget= forms.Textarea(
		attrs={'class' : 'custom-scroll' , 'id': 'observacion'}))	
	class Meta:
		model = Modelo
		
