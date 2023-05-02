from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre_categoria= models.CharField(verbose_name="nombre_categoria",null=False,blank=False
                                       ,max_length=50,unique=True)
    class meta:
        verbose_name_plural = "categoria"
        db_table = "categoria"
        verbose_name = "categoria"

class Producto(models.Model):
    nombre= models.CharField(verbose_name="nombre",null=False,blank=False,max_length=50)
    descripcion= models.CharField(verbose_name="descripcion",null=False,blank=False,max_length=100)
    precio_unitario= models.IntegerField(verbose_name="precio_unitario",null=False,blank=False)
    detalle_producto= models.CharField(verbose_name="detalle_producto",null=False,blank=False,max_length=200)
    categoria_id= models.ForeignKey(Categoria,on_delete=models.CASCADE,null=True)
    class meta:
        verbose_name_plural = "producto"
        db_table = "producto"
        verbose_name = "producto"

class Inventario(models.Model):
    producto_id = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad= models.IntegerField(verbose_name="cantidad",null=False,blank=False)
    class meta:
        verbose_name_plural = "inventario"
        db_table = "inventario"
        verbose_name = "inventario"
