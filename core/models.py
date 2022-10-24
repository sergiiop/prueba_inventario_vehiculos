from django.db import models

# Create your models here.
class Propietarios(models.Model):
    TIPO_DOCUMENTO = (
        ('CC', 'CC'),
        ('TI', 'TI'),
        ('CE', 'CE'),
        )
    nombre_apellidos=models.CharField(max_length=100)
    tipo_documento=models.CharField(max_length=2, choices=TIPO_DOCUMENTO, default='CC')
    documento=models.IntegerField(unique=True)
    direccion=models.CharField(max_length=100)
    telefono=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre_apellidos

class Vehiculos(models.Model):
    placa=models.CharField(max_length=7, unique=True)
    marca=models.CharField(max_length=20)
    modelo=models.CharField(max_length=20)
    año=models.IntegerField(blank=True)
    color=models.CharField(max_length=10,blank=True)
    propietario=models.ForeignKey(Propietarios, on_delete=models.CASCADE)
    observaciones=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.propietario