from os import error

from django.shortcuts import render,redirect
from django.views import View  
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,aauthenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User

class Vregistro(View):

    def get(self,request):
        form = UserCreationForm()
        return render(request, 'registro.html', {'form': form})
    
    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('Home')
        else:
            for mensaje in form.error_messages:
                messages.error(request,form.error_messages[mensaje])
            return render(request, 'registro.html', {'form': form})
        
def logear(request):
    if request.method=="POST":
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contrasena = form.cleaned_data.get("password")
            usuario = aauthenticate(username = nombre_usuario, password = contrasena)
            if usuario is not None:
                login(request,usuario)
                return redirect('Home')
            else:
                messages.error(request,"usuario no valido")
        else:
            messages.error(request,"informacion incorrecta")
    form = AuthenticationForm()
    return render(request,"login.html",{"form":form})

def cerrar_sesion(request):
    logout(request)
    return redirect('Home')
