from django.contrib import admin
from .models import Producto, Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'disponible', 'imagen', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('disponible', 'categoria')