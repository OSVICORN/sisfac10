from django.shortcuts import render
from django.utils.dateparse import parse_date
from datetime import timedelta, datetime
from django.utils import timezone

from ped.models import PedidoEnc, PedidoDet
from fac.models import Cliente

def imprimir_prediccion(request,f1,f2):
    template_name="inf/prediccion_imprimir.html"

    f1=parse_date(f1)
    f2=parse_date(f2)
    f2=f2 + timedelta(days=1)
    print(f1,f2)
    
    enc = PedidoEnc.objects.filter(fecha__gte=f1,fecha__lt=f2)
    
    print(enc.cliente.id)

    #print(datetime.utcnow())
    #datetime.utcnow().replace(tzinfo=timezone.utc)
    #print(datetime.utcnow())
    
    f2=f2 - timedelta(days=1)
    
    context = {
        'request':request,
        'f1':f1,
        'f2':f2,
        'enc':enc
    }

    return render(request,template_name,context)
