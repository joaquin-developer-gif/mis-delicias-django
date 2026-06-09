"""
Archivo principal para ejecutar comandos administrativos de Django.
Ejemplos:
python manage.py runserver
python manage.py migrate
"""

import os
import sys


def main():
    """Configura Django y ejecuta comandos desde la terminal."""

    # Indica a Django qué archivo de configuración debe usar.
    # En este caso usa: ingenieria_tp/settings.py
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ingenieria_tp.settings')

    try:
        # Importa la función que ejecuta comandos como runserver, migrate, etc.
        from django.core.management import execute_from_command_line

    except ImportError as exc:
        # Error común cuando Django no está instalado
        # o no está activado el entorno virtual.
        raise ImportError(
            "No se pudo importar Django. Verificá que esté instalado "
            "y que el entorno virtual esté activado."
        ) from exc

    # Ejecuta el comando escrito en la terminal.
    # Ejemplo: python manage.py runserver
    execute_from_command_line(sys.argv)


# Ejecuta main() solo si este archivo se corre directamente.
if __name__ == '__main__':
    main()