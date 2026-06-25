from django.db import models

# Create your models here.
class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoriaprod'
        verbose_name_plural='categoriasprod'

    def __str__(self):
        return self.nombre 
    
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categoria=models.ForeignKey(CategoriaProd,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='tienda', null =True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name='productos'
        verbose_name_plural='productos'

    def __str__(self):
        return self.nombre





    
