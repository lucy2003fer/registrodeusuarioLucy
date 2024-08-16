from django.db import models

# Create your models here.


class Persona(models.Model):
    
    ESTADO_CHOICE = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo')
    ]
    nombre = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=50)
    fecha_Creacion = models.DateField(auto_now=True)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICE, default='activo')