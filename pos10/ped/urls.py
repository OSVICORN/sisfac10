from django.urls import path, include

from .views import PedidoView, pedidos, PedidoDetDelete,\
    ProductoView
    
    #, \
    #borrar_detalle_pedido

from .reportes import imprimir_pedido_recibo, imprimir_pedido_list

urlpatterns = [
    path('pedidos/',PedidoView.as_view(), name="pedido_list"),
    path('pedidos/new',pedidos, name="pedido_new"),
    path('pedidos/edit/<int:id>',pedidos, name="pedido_edit"),
    path('pedidos/<int:pedido_id>/delete/<int:pk>',PedidoDetDelete.as_view(), name="pedidos_del"),
    
    path('pedidos/buscar-producto',ProductoView.as_view(), name="pedido_producto"),

    #path('pedidos/borrar-detalle/<int:id>',borrar_detalle_pedido, name="pedido_borrar_detalle"),

    path('pedidos/imprimir/<int:id>',imprimir_pedido_recibo, name="pedido_one"),

    path('pedidos/imprimir-todas/<str:f1>/<str:f2>',imprimir_pedido_list, name="pedido_imprimir_all"),

]