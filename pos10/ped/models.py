from django.db import models

#Para los signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

from bases.models import ClaseModelo2
from inv.models import Producto
from fac.models import Cliente

class PedidoEnc(ClaseModelo2):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.id)

    def save(self):
        self.total = self.sub_total - self.descuento
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
        self.sub_total = float(float(int(self.cantidad)) * float(self.precio))
        self.total = self.sub_total - float(self.descuento)
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
