from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from blog.models import Post

# from ProyectoWeb.blog.models import Post
# from servicios.models import Servicio

def home(request):
    return render(request, "ProyectoWebApp/home.html")

# def servicios(request):
#     servi=Servicio.objects.all()
#     return render(request,"ProyectoWebApp/servicios.html",{"servi":servi})


def blog(request):
    Posts=Post.objects.all().order_by('-creado')
    return render(request,"ProyectoWebApp/blog.html",{"Posts":Posts})

# def contactos(request):
#     return render(request,"ProyectoWebApp/contactos.html")

# def tienda(request):
#     return render(request,"ProyectoWebApp/tienda.html")


def contactos(request):
    if request.method == 'POST':
        asunto=request.POST.get("asunto")
        email=request.POST.get("email")
        mensaje=request.POST.get("mensaje")
        mensaje_user = f"""Email del usuario:{email} Mensaje:{mensaje}"""
        send_mail(
            asunto,
            mensaje_user,
            settings.EMAIL_HOST_USER,
            ["tgaleano882@gmail.com"],
            fail_silently=False
        )
        return render(request,"ProyectoWebApp/contactos.html", {"valido": True
        })
    return render (request,"ProyectoWebApp/contactos.html")        



 