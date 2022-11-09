from django import forms
from .models import Vehiculos,Propietarios

class FormVehiculo(forms.ModelForm):
    class Meta:
        model = Vehiculos
        fields = '__all__'

    def __init__(self, *args, **kwards):
        super(FormVehiculo, self).__init__(*args, **kwards)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += 'input-form-vehiculo'
            else:
                field.widget.attrs['class'] = 'input-form-vehiculo'

class FormPropietarios(forms.ModelForm):
    class Meta:
        model = Propietarios
        fields = '__all__'

    def __init__(self, *args, **kwards):
        super(FormPropietarios, self).__init__(*args, **kwards)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += 'input-form-vehiculo'
            else:
                field.widget.attrs['class'] = 'input-form-vehiculo'
