from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from cliente.models import Categoria, Inventario

# Create your views here.

class InventarioController:
    @login_required(login_url='login')
    def getAllInventario(request):
        inventario = Inventario.objects.select_related('producto_id').filter(cantidad__gt=0)
        # print(inventario)
        categorias = Categoria.objects.all() 
        return render(request,'clientes/menu.html',context={'inventario':inventario,'categorias':categorias})
    


    