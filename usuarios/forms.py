from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = [
            'username',
            'email',
            'telefono',
            'direccion',
            'password1',
            'password2',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }


