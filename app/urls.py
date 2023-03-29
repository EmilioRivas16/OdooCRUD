from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('data', views.get, name='get'),

    path('index', views.listado, name='listado'),
    path('agregar', views.form_agregar, name='agregar'),
    path('ejecutar_agregar/<str:name>/<str:precio>/<str:existencia>/<str:descripcion>', views.agregar, name='ejecutar_agregar'),
    path('modificar/<int:id>', views.form_modificar, name='modificar'),
    path('ejecutar_modificar/<int:id>/<str:name>/<str:precio>/<str:existencia>/<str:descripcion>', views.modificar, name='ejecutar_modificar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('detallado/<int:id>', views.detallado, name='detallado'),
]