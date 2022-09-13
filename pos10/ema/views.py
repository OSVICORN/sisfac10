from django.shortcuts import render
from django.shortcuts import redirect

from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives

from django.template.loader import get_template

from ped.models import PedidoEnc, PedidosManager

# Create your views here.

""" def crear_mail(id):
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
    return mail """

""" def enviar_bienvenida():
    mail_bienvenida = crear_mail(
        'osvicor@hotmail.com',
        'Prueba del correo',
        'ema/bienvenida.html',
        {
            'username': 'osvaldo'
        }
    )

    mail_bienvenida.send(fail_silently=False) """


def enviar_correo(self):
    asunto='Correo Enviado Automaticamente de pedidos'
    mensaje='Prueba - de correo vitalfood'
    
    send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, ['indalecioromero1@gmail.com'], fail_silently=False,)

    return redirect('ped:pedido_list')
    
    """ import smtplib , ssl
    #sender = "ventas@vitalfood.com.co"
    #password = "0Ean*l596"

    sender = "osvicor@hotmail.com"
    password = "Jose_0331"
        
    where_to_email = "eterniasas@gmail.com"
    theme = "this is subject"
    message = "this is your message, say hi to reciever"
        
    sender_password = password
    session = smtplib.SMTP_SSL("smtp.office365.com",587)
    session.login(sender, sender_password)
    msg = f'From: {sender}\r\nTo: {where_to_email}\r\nContent-Type: text/plain; charset="utf-8"\r\nSubject: {theme}\r\n\r\n'
    msg += message
    session.sendmail(sender, where_to_email, msg.encode('utf8'))
    #session.quit()
    return redirect('ped:pedido_list')

 """