from django.urls import path
from .views import listarPersonas, crearPersona

urlpatterns = [
    path('',listarPersonas, name='listarPersonas'),
    path('crear/',crearPersona, name='crearPersona'),
]