from django.urls import path
from django.views.generic import TemplateView
from .views import InventarioController,CarritoController

urlpatterns=[
    path('menu',InventarioController.getAllInventario,name='menu'),
    path('add_carrito',CarritoController.add_carrito,name='add_carrito'),
    path('detalle/<int:id_prod>/',InventarioController.detalle_producto,name='detalle'),
]