import imp
from django.shortcuts import render
from django.shortcuts import redirect

from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives

from django.template.loader import get_template

from ped.models import PedidoEnc, PedidosManager

# Create your views here.

def crear_mail(id):
    template = 'ema/bienvenida.html'
    dato = PedidoEnc.objects.filter(id=id)
    print(dato)
    email = 'osvicor@hotmail.com'
    #content = template.render(context)

    mail = EmailMultiAlternatives(
        'subject = subject',
        'asdasdASDAS',
        from_email = settings.EMAIL_HOST_USERNAME,
        to=[email]
    )
    print(mail)
    mail.attach_alternative(content, 'text/html')
    return mail

def enviar_bienvenida():
    mail_bienvenida = crear_mail(
        'osvicor@hotmail.com',
        'Prueba del correo',
        'ema/bienvenida.html',
        {
            'username': 'osvaldo'
        }
    )

    mail_bienvenida.send(fail_silently=False)


def enviar_correo(self):
    asunto='Pedidos'
    mensaje='Prueba'
    remitente='ventas@vitalfood.com.co'
    
    send_mail(asunto, mensaje, remitente, ['osvicor@hotmail.com'], fail_silently=False,)

    return redirect('ped:pedido_list')