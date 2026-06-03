from django.urls import path
from .views import registro, iniciar_sesion, cerrar_sesion

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', iniciar_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
]


# Importa path para definir las rutas de esta app
from django.urls import path

# Importa las vistas que se ejecutan en cada ruta
from .views import registro, iniciar_sesion, cerrar_sesion


# Rutas de autenticación de la app
urlpatterns = [
    # Ruta para registrar un nuevo usuario
    path('registro/', registro, name='registro'),

    # Ruta para iniciar sesión
    path('login/', iniciar_sesion, name='login'),

    # Ruta para cerrar sesión
    path('logout/', cerrar_sesion, name='logout'),
]