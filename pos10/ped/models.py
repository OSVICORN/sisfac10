from operator import mod
from django.db import models

#managers
from .managers import PedidosManager

#Para los signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

from bases.models import ClaseModelo2
from inv.models import Producto
from fac.models import Cliente, Repartidor

class PedidoEnc(ClaseModelo2):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    repartidor = models.ForeignKey(Repartidor, on_delete=models.CASCADE, default=1)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)
    facturado = models.CharField(max_length=1, default='P')
    mail_repartidor = models.IntegerField(default=False)
    mail_cliente = models.IntegerField(default=False)

    objects = PedidosManager()

    def __str__(self):
        return '{}'.format(self.id)

    def save(self):
        self.total = self.sub_total - self.descuento
        self.facturado = 'P'
        super(PedidoEnc,self).save()

    class Meta:
        verbose_name_plural = "Encabezado Pedidos"
        verbose_name="Encabezado Pedido"
        permissions = [
            ('sup_caja_pedidoenc','Permisos de Supervisor de Pedidos Encabezado')
        ]

class PedidoDet(ClaseModelo2):
    pedido = models.ForeignKey(PedidoEnc,on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad=models.BigIntegerField(default=0)
    precio=models.FloatField(default=0)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self):
        self.sub_total = float(self.cantidad) * float(self.precio)
        self.total = float(self.sub_total) - float(self.descuento)
        super(PedidoDet, self).save()
    
    class Meta:
        verbose_name_plural = "Detalle Pedidos"
        verbose_name="Detalle Pedido"
        permissions = [
            ('sup_caja_pedidodet','Permisos de Supervisor de Pedidos Detalle')
        ]

@receiver(post_save, sender=PedidoDet)
def detalle_ped_guardar(sender,instance,**kwargs):
    pedido_id = instance.pedido.id
    producto_id = instance.producto.id

    enc = PedidoEnc.objects.get(pk=pedido_id)
    if enc:
        sub_total = PedidoDet.objects \
            .filter(pedido=pedido_id) \
            .aggregate(sub_total=Sum('sub_total')) \
            .get('sub_total',0.00)
        
        descuento = PedidoDet.objects \
            .filter(pedido=pedido_id) \
            .aggregate(descuento=Sum('descuento')) \
            .get('descuento',0.00)
        
        enc.sub_total = sub_total
        enc.descuento = descuento
        enc.save()

    prod=Producto.objects.filter(pk=producto_id).first()
    if prod:
        cantidad = int(prod.existencia) - int(instance.cantidad)
        prod.existencia = cantidad
        prod.save()

@receiver(post_delete, sender=PedidoDet)
def detalle_pedido_borrar(sender,instance, **kwargs):
    id_producto = instance.producto.id
    id_pedido = instance.pedido.id

    enc = PedidoEnc.objects.filter(pk=id_pedido).first()
    if enc:
        sub_total = PedidoDet.objects.filter(pedido=id_pedido).aggregate(Sum('sub_total'))
        descuento = PedidoDet.objects.filter(pedido=id_pedido).aggregate(Sum('descuento'))
        enc.sub_total=sub_total['sub_total__sum']
        enc.descuento=descuento['descuento__sum']
        enc.save()
    
    prod=Producto.objects.filter(pk=id_producto).first()
    if prod:
        cantidad = int(prod.existencia) + int(instance.cantidad)
        prod.existencia = cantidad
        prod.save()