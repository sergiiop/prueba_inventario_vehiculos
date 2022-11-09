from django.db import models

# Create your models here.
class Propietarios(models.Model):
    TIPO_DOCUMENTO = (
        ('CC', 'CC'),
        ('TI', 'TI'),
        ('CE', 'CE'),
        )
    nombre_apellidos=models.CharField(max_length=100, null=False)
    tipo_documento=models.CharField(max_length=2, choices=TIPO_DOCUMENTO, default='CC')
    documento=models.CharField(max_length=15, null=False, unique=True)
    direccion=models.CharField(max_length=100,null=True)
    telefono=models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.nombre_apellidos

class Marca(models.Model):
    descripcion=models.CharField(max_length=256, null=False)
    def __str__(self):
        return self.descripcion

class Modelo(models.Model):
    descripcion=models.CharField(max_length=256, null=False)
    marca=models.ForeignKey(Marca, on_delete=models.CASCADE)
    def __str__(self):
        return self.descripcion

class Vehiculos(models.Model):
    placa=models.CharField(max_length=7, unique=True)
    marca=models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo=models.ForeignKey(Modelo, on_delete=models.CASCADE)
    año=models.CharField(max_length=4, null=False)
    color=models.CharField(max_length=20, null=False)
    propietario=models.ForeignKey(Propietarios, on_delete=models.CASCADE)
    observaciones=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.propietario