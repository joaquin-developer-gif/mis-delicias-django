from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent


# Clave secreta del proyecto.
# En producción no debe estar escrita directamente en el código.
SECRET_KEY = 'django-insecure-&!w37_e^yw2b+ku$k=ki1&_#o2fn=zv28v00%fe43$3jieonc='

# Modo desarrollo activado.
# En producción debe estar en False.
DEBUG = True

# Hosts permitidos para ejecutar el proyecto.
# Vacío significa que solo se usa en desarrollo local.
ALLOWED_HOSTS = []


# Aplicaciones instaladas en el proyecto
INSTALLED_APPS = [
    # Apps internas de Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps propias del proyecto
    'core',
    'reposteria',
    'usuarios',
]


# Middlewares: procesan las peticiones y respuestas del sistema
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Archivo principal de rutas del proyecto
ROOT_URLCONF = 'ingenieria_tp.urls'


# Configuración de templates HTML
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # Django buscará templates dentro de cada app
        'DIRS': [],
        'APP_DIRS': True,

        # Procesadores de contexto disponibles en los templates
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Configuración WSGI para desplegar la aplicación
WSGI_APPLICATION = 'ingenieria_tp.wsgi.application'


# Base de datos del proyecto
DATABASES = {
    'default': {
        # Usa SQLite, ideal para desarrollo y trabajos prácticos
        'ENGINE': 'django.db.backends.sqlite3',

        # Archivo donde se guarda la base de datos
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Validaciones de seguridad para contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        # Evita contraseñas parecidas a los datos del usuario
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        # Exige una longitud mínima
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        # Evita contraseñas demasiado comunes
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        # Evita contraseñas solo numéricas
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Configuración de idioma y zona horaria
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True


# Ruta base para archivos estáticos: CSS, JS e imágenes del frontend
STATIC_URL = '/static/'


# Tipo de ID automático para los modelos
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Modelo de usuario personalizado
AUTH_USER_MODEL = 'usuarios.Usuario'


# Configuración para archivos subidos por usuarios
MEDIA_URL = '/media/'

# Carpeta física donde se guardan los archivos multimedia
MEDIA_ROOT = BASE_DIR / 'media'