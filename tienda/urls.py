from django.urls import path
from .views import (ProductoListView, ProductoCreateView,ProductoDeleteView, ProductoUpdateView,CategoriaListView, 
                    CategoriaCreateView, CategoriaDeleteView, InventarioListView, buscar_producto, buscar_inventario)

urlpatterns=[
    # <---------------urls de producto------------>
    path('productos/', ProductoListView, name='producto-list'),
    path('productos/buscar/', buscar_producto, name='buscar-producto'),
    path('inventario/buscar/', buscar_inventario, name='buscar-inventario'),
    path('producto/create/', ProductoCreateView, name='producto-create'),
    path('producto/delete/<int:id>', ProductoDeleteView, name='producto-delete'),
    path('producto/update/<int:id>', ProductoUpdateView, name='producto-update'),
    # <---------------urls de categoria------------>
    path('categoria/', CategoriaListView, name='categoria-list'),
    path('categoria/create/', CategoriaCreateView, name='categoria-create'),
    path('categoria/delete/<int:id>', CategoriaDeleteView, name='categoria-delete'),

    path('inventario/', InventarioListView, name='inventario-list'),
]