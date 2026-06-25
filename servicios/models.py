from django.db import models

class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=150)
    imagen=models.ImageField(upload_to='servicios')
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo
