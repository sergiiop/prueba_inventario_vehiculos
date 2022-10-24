from django import forms
from .models import Vehiculos,Propietarios

class FormVehiculo(forms.ModelForm):
    class Meta:
        model = Vehiculos
        fields=['placa','marca', 'modelo', 'año', 'color', 'propietario']
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'input-form-vehiculo'}),
            'marca': forms.TextInput(attrs={'class': 'input-form-vehiculo'}),
            'modelo': forms.TextInput(attrs={'class': 'input-form-vehiculo'}),
            'año': forms.TextInput(attrs={'class': 'input-form-vehiculo'}),
            'color': forms.TextInput(attrs={'class': 'input-form-vehiculo'}),
        }

class FormPropietarios(forms.ModelForm):
    class Meta:
        model = Propietarios
        fields= ['nombre_apellidos','tipo_documento', 'documento', 'direccion', 'telefono']
        widgets = {
            'nombre_apellidos': forms.TextInput(attrs={'class': 'input-form-vehiculo'}),
            'documento': forms.TextInput(attrs={'class': 'input-form-vehiculo'}),
            'direccion': forms.TextInput(attrs={'class': 'input-form-vehiculo'}),
            'telefono': forms.TextInput(attrs={'class': 'input-form-vehiculo'}),
        }