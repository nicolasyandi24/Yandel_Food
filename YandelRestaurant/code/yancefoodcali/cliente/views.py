from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Carrito_compra,Usuario
from django.contrib import messages


from cliente.models import Categoria, Inventario

# Create your views here.

class InventarioController:
    @login_required(login_url='login')
    def getAllInventario(request):
        inventario = Inventario.objects.select_related('producto_id').filter(cantidad__gt=0)
        carrito={}
        # print(inventario)
        categorias = Categoria.objects.all()
        if request.user.is_authenticated:
            usuario = Usuario.objects.get(credenciales=request.user.id)
            carrito = Carrito_compra.objects.filter(fk_usuario=usuario.id,estado=True)
            print(carrito)
        return render(request,'clientes/menu.html',context={'inventario':inventario,
                                                            'categorias':categorias,
                                                            'carrito':carrito})
    
    @login_required
    def detalle_producto(request,id_prod):
        producto = Inventario.objects.select_related('producto_id').get(producto_id=id_prod)
        return render(request,'clientes/detalle_producto.html',{'detalle':producto})

class CarritoController:
    @login_required(login_url='login')
    def add_carrito(request):
        inv_id = request.POST.get('inv_id')
        user_id = request.POST.get('user_id')
        cantidad = request.POST.get('cantidad')
        try:
            inv = Inventario.objects.get(pk=inv_id)
            usuario = Usuario.objects.select_related('credenciales').get(credenciales=user_id)
            carrito = Carrito_compra(fk_producto=inv.producto_id,cantidad=cantidad,
                                    fk_usuario=usuario,valor=int(cantidad)*int(inv.producto_id.precio_unitario))
            carrito.save()
        except Exception as e:
            print(e.args)
        return redirect('menu')

    @login_required(login_url='login')
    def add_carrito(request):
        inv_id = request.POST.get('inv_id')
        user_id = request.POST.get('user_id')
        cantidad = request.POST.get('cantidad')
        try:
            inv = Inventario.objects.get(pk=inv_id)
            usuario = Usuario.objects.select_related('credenciales').get(credenciales=user_id)
            carrito = Carrito_compra(fk_producto=inv.producto_id,cantidad=cantidad,
                                    fk_usuario=usuario,valor=int(cantidad)*int(inv.producto_id.precio_unitario))
            carrito.save()
            messages.success(request,'Producto agregado')
        except Exception as e:
            print(e.args)
            messages.error(request,'No se pudo agrgar el prodcuto')
        return redirect('menu')

    


    