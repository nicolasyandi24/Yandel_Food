from django.urls import path
from django.views.generic import TemplateView
from .views import InventarioController

urlpatterns=[
    path('menu/',InventarioController.getAllInventario,name='menu')
]