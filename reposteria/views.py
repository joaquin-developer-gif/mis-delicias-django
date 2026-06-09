from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm


def productos(request):
    productos = Producto.objects.all()

    return render(request, 'reposteria/productos.html', {
        'productos': productos
    })


def producto_detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    return render(request, 'reposteria/producto_detalle.html', {
        'producto': producto
    })


def producto_crear(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm()

    return render(request, 'reposteria/producto_form.html', {
        'form': form,
        'titulo': 'Crear producto'
    })


def producto_editar(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)

        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'reposteria/producto_form.html', {
        'form': form,
        'titulo': 'Editar producto'
    })


def producto_eliminar(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        producto.delete()
        return redirect('productos')

    return render(request, 'reposteria/producto_confirm_delete.html', {
        'producto': producto
    })