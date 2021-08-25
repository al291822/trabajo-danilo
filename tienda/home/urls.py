from django.urls import path
from . import views

urlpatterns = [
    path('lista_producto/', views.vista_lista_producto, name='vista_lista_producto'),
    path('agregar_producto/', views.vista_agregar_producto, name='vista_agregar_producto'),
    path('ver_producto/<int:id_prod>/', views.vista_ver_producto, name='vista_ver_producto'),
    path('editar_producto/<int:id_prod>/', views.vista_editar_producto, name = 'vista_editar_producto'),
    path('eliminar_producto/<int:id_prod>/', views.vista_eliminar_producto, name='vista_eliminar_producto'),
    ]


