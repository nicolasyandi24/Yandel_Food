from django.shortcuts import render

from cliente.models import Categoria, Inventario

# Create your views here.

class InventarioController:
    def getAllInventario(request):
        inventario = Inventario.objects.select_related('producto_id').filter(cantidad__gt=0)
        print(inventario)
        categorias = Categoria.objects.all()
        # inventario_final = {}
        # for cat in categorias:
        #     inventario_final[cat.nombre_categoria] = get_inventario_by_categoria(inventario,cat.id)

        return render(request,'clientes/menu.html',context={'inventario':inventario,'categorias':categorias})
    
# def get_inventario_by_categoria(inventario:Inventario,id_categoria):
#     valores=[]
#     for valor in inventario:
#         if valor.categoria_id == id_categoria:
#             valores.append(valor)
#     return valores



    