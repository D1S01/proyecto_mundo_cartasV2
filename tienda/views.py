from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria, Inventario
from .forms import ProductoForm, CategoriaForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

# Create your views here.

# <---------------vistas de producto------------>
@login_required
def ProductoListView(request):
    return render(request, 'tienda/producto/producto_list.html', {'productos':Producto.objects.all()})

def InventarioListView(request):
    return render(request, 'tienda/inventario/inventario_list.html', {'productos':Producto.objects.all()})

def ProductoCreateView(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES or None)
        if form.is_valid():
            producto = form.save()
            stock = request.POST.get('stock')
            Inventario.objects.create(producto=producto, stock=stock)
            return redirect('producto-list')
    else:
        form = ProductoForm()
    return render(request, 'tienda/producto/producto_form.html', {'form': form, 'action': 'Crear'})

@login_required
def ProductoDeleteView(request, id):
    producto=get_object_or_404(Producto, pk=id)
    if request.method=="POST":
        producto.delete()
        return redirect('producto-list')
    return render(request, 'tienda/producto/producto_delete.html')

@login_required
def ProductoUpdateView(request, id):
    producto = get_object_or_404(Producto, pk=id) 
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES or None, instance=producto)
        if form.is_valid():
            producto = form.save()
            stock = request.POST.get('stock')
            Inventario.objects.update_or_create(producto=producto, defaults={'stock': stock})
            return redirect('producto-list')
    else:
        form = ProductoForm(instance=producto, initial={'stock': producto.inventario.stock})
    return render(request, 'tienda/producto/producto_form.html', {'form': form, 'action': 'Modificar'})
# <---------------vistas de categoria------------>
@login_required
def CategoriaListView(request):
    return render(request, 'tienda/categoria/categoria_list.html', {'categorias':Categoria.objects.all()})

@login_required
def CategoriaCreateView(request):
    if request.method=="POST":
        form=CategoriaForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('categoria-list')
    else:
        form=CategoriaForm()
    return render(request, 'tienda/categoria/categoria_form.html', {'form':form, 'action':'Crear'})

@login_required
def CategoriaDeleteView(request, id):
    categoria=get_object_or_404(Categoria, pk=id)
    if request.method=="POST":
        categoria.delete()
        return redirect('categoria-list')
    return render(request, 'tienda/categoria/categoria_delete.html')


def buscar_producto(request):
    query = request.GET.get('buscar', '').strip()
    productos = Producto.objects.filter(nombre__icontains=query) if query else Producto.objects.all()
    return render(request, 'tienda/producto/producto_list.html', {
        'productos': productos,
        'query': query
    })

def buscar_inventario(request):
    query = request.GET.get('buscar', '').strip()
    productos = Producto.objects.filter(nombre__icontains=query) if query else Producto.objects.all()
    return render(request, 'tienda/inventario/inventario_list.html', {
        'productos': productos,
        'query': query
    })
