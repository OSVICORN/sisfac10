from django import models

class PedidosManager(models.Manager):

    def lista_pedidos_rango_fechas

        return self.all()