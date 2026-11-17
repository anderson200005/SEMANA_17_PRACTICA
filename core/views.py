from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Libro, Prestamo
from .forms import CategoriaForm, LibroForm, PrestamoForm

# --- CATEGORÍAS ---
def lista_categorias(request):
    items = Categoria.objects.all()
    return render(request, 'core/lista_categorias.html', {'items': items})

def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_categorias')
    return render(request, 'core/form_general.html', {'form': form, 'titulo': 'Nueva Categoría'})

def editar_categoria(request, pk):
    item = get_object_or_404(Categoria, pk=pk)
    form = CategoriaForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('lista_categorias')
    return render(request, 'core/form_general.html', {'form': form, 'titulo': 'Editar Categoría'})

def eliminar_categoria(request, pk):
    item = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('lista_categorias')
    return render(request, 'core/eliminar_general.html', {'item': item, 'cancel_url': 'lista_categorias'})

# --- LIBROS ---
def lista_libros(request):
    items = Libro.objects.all()
    return render(request, 'core/lista_libros.html', {'items': items})

def crear_libro(request):
    form = LibroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_libros')
    return render(request, 'core/form_general.html', {'form': form, 'titulo': 'Nuevo Libro'})

def editar_libro(request, pk):
    item = get_object_or_404(Libro, pk=pk)
    form = LibroForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('lista_libros')
    return render(request, 'core/form_general.html', {'form': form, 'titulo': 'Editar Libro'})

def eliminar_libro(request, pk):
    item = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('lista_libros')
    return render(request, 'core/eliminar_general.html', {'item': item, 'cancel_url': 'lista_libros'})

# --- PRÉSTAMOS ---
def lista_prestamos(request):
    items = Prestamo.objects.all()
    return render(request, 'core/lista_prestamos.html', {'items': items})

def crear_prestamo(request):
    form = PrestamoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_prestamos')
    return render(request, 'core/form_general.html', {'form': form, 'titulo': 'Nuevo Préstamo'})

def editar_prestamo(request, pk):
    item = get_object_or_404(Prestamo, pk=pk)
    form = PrestamoForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('lista_prestamos')
    return render(request, 'core/form_general.html', {'form': form, 'titulo': 'Editar Préstamo'})

def eliminar_prestamo(request, pk):
    item = get_object_or_404(Prestamo, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('lista_prestamos')
    return render(request, 'core/eliminar_general.html', {'item': item, 'cancel_url': 'lista_prestamos'})