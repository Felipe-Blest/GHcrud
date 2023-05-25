from django.db import models

class Persona(models.Model):
    rut = models.CharField(db_column='rut', blank=False, max_length=20, primary_key=True)
    nombre = models.CharField(db_column='nombre', blank=False, max_length=20)
    apellido = models.CharField(db_column='apellido', blank=False, max_length=30)

    def __str__(self):
        return "%s" %(self.nombre)
        
    class Meta:
        db_table='persona'