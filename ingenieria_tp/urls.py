from django.contrib import admin
from django.urls import path

from core.views import home
from reposteria.views import productos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('productos/', productos, name='productos'),
]