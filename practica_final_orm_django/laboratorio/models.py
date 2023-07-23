from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

def validate_year(value):
    min_date = date(2015, 1, 1)
    max_date = date(2023, 12, 31)

    if value < min_date:
        raise ValidationError('La fecha no puede ser antes de 2015.')
    elif value > max_date:
        raise ValidationError('La fecha no puede ser después de 2023.')

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=128)
    ciudad = models.CharField(max_length=128)
    pais = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=128)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=128)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField(default=date(2015, 1, 1), validators=[validate_year])
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.nombre