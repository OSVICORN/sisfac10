from django.db import models

#Para los signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

from bases.models import ClaseModelo, ClaseModelo2
from inv.models import Producto

class Barrio(ClaseModelo):
    descripcion = models.CharField(
        max_length=60,
        help_text='Nombre del Barrio',
        unique=True
        )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Barrio, self).save()

    class Meta:
        verbose_name_plural = "Barrios"

class Ruta(ClaseModelo):
    nombre = models.CharField(
        max_length=60,
        help_text='Nombre de la Ruta',
        unique=True
        )
    descripcion = models.CharField(
        max_length=60,
        help_text='Descripción de la Ruta',
        unique=True
        )

    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre = self.nombre.upper()
        self.descripcion = self.descripcion.upper()
        super(Ruta, self).save()

    class Meta:
        verbose_name_plural = "Rutas"

class Cliente(ClaseModelo):
    NAT='Natural'
    JUR='Jurídica'
    TIPO_CLIENTE = [
        (NAT,'Natural'),
        (JUR,'Jurídica')
    ]
    MAS = 'Masculino'
    FEM = 'Femenino'
    OTR = 'Otro'
    GENERO_CLIENTE = [
        (MAS,'Masculino'),
        (FEM,'Femenino'),
        (OTR,'Otro')
    ]
    EMP = 'Corporativo/Empresarial/Mayorista'
    NAT = 'Natural/Detail/Minorista'
    INS = 'Institucional/Público/Fundaciones'
    TEN = 'Tienda/Minimercado/Negocio'
    SEGMENTO_CLIENTE = [
        (EMP,'Corporativo/Empresarial/Mayorista'),
        (NAT,'Natural/Detail/Minorista'),
        (INS,'Institucional/Público/Fundaciones'),
        (TEN,'Tienda/Minimercado/Negocio')
    ]
    tipo=models.CharField(
        max_length=10,
        choices=TIPO_CLIENTE,
        default=NAT
    )
    documento = models.CharField(max_length=10, unique=True)
    nombres = models.CharField(
        max_length=100
    )
    apellidos = models.CharField(
        max_length=100
    )
    segmento = models.CharField(max_length=60,choices=SEGMENTO_CLIENTE, default=NAT)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=10,choices=GENERO_CLIENTE, default=MAS)
    direccion = models.CharField(max_length=200)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE, default=1)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, default=1)
    celular = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    correo = models.EmailField(max_length=250)
    razonsocial = models.CharField(max_length=120, blank=True)
    actividad = models.CharField(max_length=20, blank=True) 
    replegal = models.CharField(max_length=60, blank=True)
    contacto = models.CharField(max_length=60, blank=True)
    celcontacto = models.CharField(max_length=10, blank=True)
    correocontacto = models.EmailField(max_length=250, blank=True)
    telfijo = models.CharField(max_length=10, blank=True)
    cupocredito = models.PositiveIntegerField(default=0)
    trato_datos = models.BooleanField(default=False)

    def __str__(self):
        return '{} {}'.format(self.apellidos,self.nombres)

    def save(self, *args, **kwargs):
        self.nombres = self.nombres.upper()
        self.apellidos = self.apellidos.upper()
        super(Cliente, self).save( *args, **kwargs)

    class Meta:
        verbose_name_plural = "Clientes"
    
class FacturaEnc(ClaseModelo2):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.id)

    def save(self):
        self.total = self.sub_total - self.descuento
        super(FacturaEnc,self).save()

    class Meta:
        verbose_name_plural = "Encabezado Facturas"
        verbose_name="Encabezado Factura"
        permissions = [
            ('sup_caja_facturaenc','Permisos de Supervisor de Caja Encabezado')
        ]

class FacturaDet(ClaseModelo2):
    factura = models.ForeignKey(FacturaEnc,on_delete=models.CASCADE)
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
        super(FacturaDet, self).save()
    
    class Meta:
        verbose_name_plural = "Detalles Facturas"
        verbose_name="Detalle Factura"
        permissions = [
            ('sup_caja_facturadet','Permisos de Supervisor de Caja Detalle')
        ]


@receiver(post_save, sender=FacturaDet)
def detalle_fac_guardar(sender,instance,**kwargs):
    factura_id = instance.factura.id
    producto_id = instance.producto.id

    enc = FacturaEnc.objects.get(pk=factura_id)
    if enc:
        sub_total = FacturaDet.objects \
            .filter(factura=factura_id) \
            .aggregate(sub_total=Sum('sub_total')) \
            .get('sub_total',0.00)
        
        descuento = FacturaDet.objects \
            .filter(factura=factura_id) \
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



