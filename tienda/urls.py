from django.urls import path, include
from tienda import views

urlpatterns = [
    path('tienda/', views.tienda,name="Tienda"),
]
