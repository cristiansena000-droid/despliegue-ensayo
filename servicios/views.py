from django.shortcuts import render
from servicios.models import Servicio

def servicios(request):
    servi=Servicio.objects.all()
    return render(request,"servicios.html",{"servi":servi})

