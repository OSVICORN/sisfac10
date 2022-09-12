from django.shortcuts import render,redirect
from django.views import generic

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages

from django.contrib.auth import authenticate

from bases.views import SinPrivilegios

from .models import PedidoEnc, PedidoDet
import inv.views as inv
from inv.models import Producto
from fac.models import Cliente

class VistaBaseCreate(SuccessMessageMixin,SinPrivilegios, \
    generic.CreateView):
    context_object_name = 'obj'
    success_message="Registro Agregado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class VistaBaseEdit(SuccessMessageMixin,SinPrivilegios, \
    generic.UpdateView):
    context_object_name = 'obj'
    success_message="Registro Actualizado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class PedidoView(SinPrivilegios, generic.ListView):
    model = PedidoEnc
    template_name = "ped/pedido_list.html"
    queryset = PedidoEnc.objects.filter(facturado='P')
    context_object_name = 'obj'
    permission_required="ped.view_pedidoenc"

    def get_queryset(self):
        user = self.request.user
        # print(user,"usuario")
        qs = super().get_queryset()
        for q in qs:
            pass
            #print(q.uc,q.id)
        
        if not user.is_superuser:
            qs = qs.filter(uc=user)

        for q in qs:
            pass
            #print(q.uc,q.id)

        return qs

@login_required(login_url='/login/')
@permission_required('ped.change_pedidoenc', login_url='bases:sin_privilegios')
def pedidos(request,id=None):
    template_name='ped/pedidos.html'

    detalle = {}
    clientes = Cliente.objects.filter(estado=True)
    
    if request.method == "GET":
        enc = PedidoEnc.objects.filter(pk=id).first()
        if id:
            if not enc:
                messages.error(request,'Pedido No Existe')
                return redirect("ped:pedido_list")

            usr = request.user
            if not usr.is_superuser:
                if enc.uc != usr:
                    messages.error(request,'Pedido no fue creada por usuario')
                    return redirect("ped:pedido_list")

        if not enc:
            encabezado = {
                'id':0,
                'fecha':datetime.today(),
                'cliente':0,
                'fecha_entrega':datetime.today(),
                'total': 0.00
            }
            detalle=None
        else:
            encabezado = {
                'id':enc.id,
                'fecha':enc.fecha,
                'fecha_entrega':enc.fecha_entrega,
                'cliente':enc.cliente,
                'total':enc.total
            }
        detalle=PedidoDet.objects.filter(pedido=enc)
        contexto = {"enc":encabezado,"det":detalle,"clientes":clientes}
        return render(request,template_name,contexto)
    
    if request.method == "POST":
        cliente = request.POST.get("enc_cliente")
        fecha  = request.POST.get("fecha")
        cli=Cliente.objects.get(pk=cliente)

        if not id:
            enc = PedidoEnc(
                cliente = cli,
                fecha = fecha
            )
            if enc:
                enc.save()
                id = enc.id
        else:
            enc = PedidoEnc.objects.filter(pk=id).first()
            if enc:
                enc.cliente = cli
                enc.save()

        if not id:
            messages.error(request,'No Puedo Continuar No Pude Detectar No. de Pedido')
            return redirect("ped:pedido_list")
        
        codigo = request.POST.get("codigo")
        cantidad = request.POST.get("cantidad")
        precio = request.POST.get("precio")
        s_total = request.POST.get("sub_total_detalle")
        descuento = request.POST.get("descuento_detalle")
        total = request.POST.get("total_detalle")

        prod = Producto.objects.get(codigo=codigo)
        det = PedidoDet(
            pedido = enc,
            producto = prod,
            cantidad = cantidad,
            precio = precio,
            sub_total = s_total,
            descuento = descuento,
            total = total
        )
        
        if det:
            det.save()
        
        return redirect("ped:pedido_edit",id=id)

    return render(request,template_name,contexto)

class PedidoEdit(VistaBaseEdit):
    model=PedidoEnc
    template_name="ped/pedido_list.html"
    form_class=PedidoEnc
    success_url= reverse_lazy("ped:pedido_list")
    permission_required="fac.change_pedidoenc"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form,t=t)
        return self.render_to_response(context)

@login_required(login_url="/login/")
@permission_required("ped.change_pedidoenc",login_url="/login/")
def pedidoFacturar(self, request, id):
    pedido = PedidoEnc.objects.filter(pk=id).first()
    if request.method=="POST":
        if pedido:
            pedido.facturado = 'F'
            PedidoEnc.save(request)
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")

class ProductoView(inv.ProductoView):
    template_name="ped/buscar_producto.html" 

'''
def borrar_detalle_pedido(request, id):
    template_name = "ped/pedido_borrar_detalle.html"

    det = PedidoDet.objects.get(pk=id)

    if request.method=="GET":
        context={"det":det}

    if request.method == "POST":
        usr = request.POST.get("usuario")
        pas = request.POST.get("pass")
        prd = request.POST.get("codigo")

        user =authenticate(username=usr,password=pas)

        if not user:
            return HttpResponse("Usuario o Clave Incorrecta")
        
        if not user.is_active:
            return HttpResponse("Usuario Inactivo")

        if user.is_superuser or user.has_perm("ped.sup_caja_pedidodet"):
            det.delete()
            
            return HttpResponse("ok")

        return HttpResponse("Usuario no autorizado")
    
    return render(request,template_name,context) '''

class PedidoDetDelete(SinPrivilegios, generic.DeleteView):
    permission_required = "ped.delete_pedidodet"
    model = PedidoDet
    template_name = "ped/pedidos_det_del.html"
    context_object_name = 'obj'
    success_url=reverse_lazy("ped:pedido_list")
    