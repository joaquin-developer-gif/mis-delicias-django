from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Datos adicionales', {'fields': ('telefono', 'direccion')}),
    )

    list_display = ('username', 'email', 'telefono', 'direccion', 'is_staff')
    search_fields = ('username', 'email', 'telefono')
