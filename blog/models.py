from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categoria'

    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    titulo=models.CharField(max_length=100)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="blog",null=True,blank=True)
    autor=models.ForeignKey(User,on_delete=models.CASCADE)
    categoria=models.ManyToManyField(Categoria)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'

    def __str__(self):
        return self.titulo+" "+self.contenido



