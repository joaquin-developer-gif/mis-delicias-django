from django.contrib import admin
from django.urls import path

from core.views import home
from reposteria.views import (
    productos,
    producto_detalle,
    producto_crear,
    producto_editar,
    producto_eliminar,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    path('productos/', productos, name='productos'),
    path('productos/crear/', producto_crear, name='producto_crear'),
    path('productos/<int:producto_id>/', producto_detalle, name='producto_detalle'),
    path('productos/<int:producto_id>/editar/', producto_editar, name='producto_editar'),
    path('productos/<int:producto_id>/eliminar/', producto_eliminar, name='producto_eliminar'),
]