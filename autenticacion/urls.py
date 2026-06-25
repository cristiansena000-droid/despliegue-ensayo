from django import views
from django.urls import path
from .views import Vregistro,logear,cerrar_sesion

urlpatterns = [path('autenticacion/', Vregistro.as_view(), name="Autenticacion"),
               path('logear', logear,name="logear"),
               path('cerrar_sesion', cerrar_sesion,name="cerrar_sesion")
]


