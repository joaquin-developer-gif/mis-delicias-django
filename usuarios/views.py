from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import RegistroUsuarioForm


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('productos')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'usuarios/registro.html', {
        'form': form
    })


def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('productos')
    else:
        form = AuthenticationForm()

    return render(request, 'usuarios/login.html', {
        'form': form
    })


def cerrar_sesion(request):
    logout(request)
    return redirect('home')