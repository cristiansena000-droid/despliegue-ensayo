from django.urls import path, include
from tienda import views
from . import views
app_name="carro"

urlpatterns = [
    path('agregar/<int:producto_id>/',views.agregar_producto,name= "agregar"),
    path('eliminar/<int:producto_id>/',views.eliminar_producto,name= "eliminar"),
    path('restar/<int:producto_id>/',views.restar,name= "restar"),
    path('limpiar/',views.limpiar_carro,name= "limpiar"),
    

    
]
