from django.db import models

from bases.models import ClaseModelo
from cmp.models import Proveedor, ComprasEnc

# Create your models here.

class NdebEnc(ClaseModelo):
    fecha_nota=models.DateField(null=True,blank=True)
    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    observacion=models.TextField(blank=True,null=True)
    total=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.observacion)

    def save(self):
        self.observacion = self.observacion.upper()
        if self.sub_total == None  or self.descuento == None:
            self.sub_total = 0
            self.descuento = 0
            
        self.total = self.sub_total - self.descuento
        super(NdebDet,self).save()

    class Meta:
        verbose_name_plural = "Encabezado Notas Débito"
        verbose_name="Encabezado Nota Débito"

class NdebDet(ClaseModelo):
    nota_debito=models.ForeignKey(NdebEnc,on_delete=models.CASCADE)
    factura=models.ForeignKey(ComprasEnc,on_delete=models.CASCADE)
    total=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.factura)

    def save(self):
        super(NdebDet, self).save()
    
    class Mega:
        verbose_name_plural = "Detalles Notas Débito"
        verbose_name="Detalle Nota Débito"

