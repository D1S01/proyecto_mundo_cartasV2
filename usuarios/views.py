from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Usuario
from .forms import UsuarioForm
from django.contrib.auth.decorators import login_required




def UsuarioListView(request):
    return render(request, 'usuarios/usuario_list.html', {'usuarios': Usuario.objects.all()})

def UsuarioCreateView(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario-list')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/usuario_form.html', {'form': form, 'action': 'Crear'})


def UsuarioUpdateView(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario-list')
    else:
        
        form = UsuarioForm(instance=usuario, initial={'username': usuario.user.username,})
    return render(request, 'usuarios/usuario_form.html', {'form': form, 'action': 'Modificar'})


def UsuarioDeleteView(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    if request.method == "POST":
        usuario.delete()
        return redirect('usuario-list')
    return render(request, 'usuarios/usuario_delete.html', {'usuario': usuario})



@login_required
def buscar_usuario(request):
    query = request.GET.get('buscar', '').strip()
    usuarios = Usuario.objects.filter(user__username__icontains=query) if query else Usuario.objects.all()
    return render(request, 'usuarios/usuario_list.html', {
        'usuarios': usuarios,
        'query': query
    })