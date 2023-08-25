from django.db import models

class Trabajo(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    empresa = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
