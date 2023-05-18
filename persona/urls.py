from django.urls import path
from persona import views

urlpatterns = [
    path('agregar', views.agregar),
    path('mostrar', views.mostrar),
    path('editar/<int:rut>', views.editar),
    path('actualizar/<int:rut>', views.actualizar),
    path('eliminar/<int:rut>', views.eliminar)
]
 