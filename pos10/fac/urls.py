from django.urls import path, include

from .views import BarrioView, BarrioNew, BarrioEdit, barrioInactivar, \
    RepartidorView, RepartidorNew, RepartidorEdit, repartidorInactivar, \
    RutaView, RutaNew, RutaEdit, rutaInactivar, \
    ClienteView,ClienteNew,ClienteEdit,clienteInactivar, \
    FacturaView, facturas, \
    ProductoView, \
    borrar_detalle_factura, \
    cliente_add_modify

from .reportes import imprimir_factura_recibo, imprimir_factura_list

urlpatterns = [

    
    path('barrios/',BarrioView.as_view(), name="barrio_list"),
    path('barrios/new',BarrioNew.as_view(), name="barrio_new"),
    path('barrios/<int:pk>',BarrioEdit.as_view(), name="barrio_edit"),
    path('barrios/estado/<int:id>',barrioInactivar, name="barrio_inactivar"),
    
    path('repartidores/',RepartidorView.as_view(), name="repartidor_list"),
    path('repartidores/new',RepartidorNew.as_view(), name="repartidor_new"),
    path('repartidores/<int:pk>',RepartidorEdit.as_view(), name="repartidor_edit"),
    path('repartidores/estado/<int:id>',repartidorInactivar, name="repartidor_inactivar"),

    path('rutas/',RutaView.as_view(), name="ruta_list"),
    path('rutas/new',RutaNew.as_view(), name="ruta_new"),
    path('rutas/<int:pk>',RutaEdit.as_view(), name="ruta_edit"),
    path('rutas/estado/<int:id>',rutaInactivar, name="ruta_inactivar"),
    
    path('clientes/',ClienteView.as_view(), name="cliente_list"),
    path('clientes/new',ClienteNew.as_view(), name="cliente_new"),
    path('clientes/<int:pk>',ClienteEdit.as_view(), name="cliente_edit"),
    path('clientes/estado/<int:id>',clienteInactivar, name="cliente_inactivar"),

    path('facturas/',FacturaView.as_view(), name="factura_list"),
    path('facturas/new',facturas, name="factura_new"),
    path('facturas/edit/<int:id>',facturas, name="factura_edit"),
    
    path('facturas/buscar-producto',ProductoView.as_view(), name="factura_producto"),

    path('facturas/borrar-detalle/<int:id>',borrar_detalle_factura, name="factura_borrar_detalle"),

    path('facturas/imprimir/<int:id>',imprimir_factura_recibo, name="factura_one"),

    path('facturas/imprimir-todas/<str:f1>/<str:f2>',imprimir_factura_list, name="factura_imprimir_all"),

    path('facturas/clientes/new/',cliente_add_modify,name="fac_cliente_add"),
    path('facturas/clientes/<int:pk>',cliente_add_modify,name="fac_cliente_mod"),

]