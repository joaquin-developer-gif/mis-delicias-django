from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['categoria', 'nombre', 'descripcion', 'precio', 'disponible', 'imagen']
        labels = {
            'categoria': 'Categoría',
            'nombre': 'Nombre del producto',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'disponible': 'Disponible',
            'imagen': 'Imagen del producto',
        }