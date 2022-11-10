from django import forms
from .models import Vehiculos,Propietarios, Ticket

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

class FormTicket(forms.ModelForm):
    class Meta:
        model = Ticket
        fields= '__all__'
        exclude=('estado','hora_entrada','hora_salida','valor')
