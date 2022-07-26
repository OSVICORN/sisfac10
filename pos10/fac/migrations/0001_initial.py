# Generated by Django 4.1.1 on 2022-09-05 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inv', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(help_text='Nombre del Barrio', max_length=60, unique=True)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Barrios',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('tipo', models.CharField(choices=[('Natural', 'Natural'), ('Jurídica', 'Jurídica')], default='Natural/Detail/Minorista', max_length=10)),
                ('documento', models.CharField(max_length=10, unique=True)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('segmento', models.CharField(choices=[('Corporativo/Empresarial/Mayorista', 'Corporativo/Empresarial/Mayorista'), ('Natural/Detail/Minorista', 'Natural/Detail/Minorista'), ('Institucional/Público/Fundaciones', 'Institucional/Público/Fundaciones'), ('Tienda/Minimercado/Negocio', 'Tienda/Minimercado/Negocio')], default='Natural/Detail/Minorista', max_length=60)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('genero', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], default='Masculino', max_length=10)),
                ('direccion', models.CharField(max_length=200)),
                ('celular', models.CharField(blank=True, max_length=20, null=True)),
                ('correo', models.EmailField(max_length=250)),
                ('razonsocial', models.CharField(blank=True, max_length=120)),
                ('actividad', models.CharField(blank=True, max_length=20)),
                ('replegal', models.CharField(blank=True, max_length=60)),
                ('contacto', models.CharField(blank=True, max_length=60)),
                ('celcontacto', models.CharField(blank=True, max_length=10)),
                ('correocontacto', models.EmailField(blank=True, max_length=250)),
                ('telfijo', models.CharField(blank=True, max_length=10)),
                ('cupocredito', models.PositiveIntegerField(default=0)),
                ('trato_datos', models.BooleanField(default=False)),
                ('barrio', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fac.barrio')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Repartidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('identificacion', models.CharField(help_text='Identificación', max_length=12, unique=True)),
                ('apellidos', models.CharField(help_text='Apellidos del Repartidor', max_length=30, unique=True)),
                ('nombres', models.CharField(help_text='Nombres del Repartidor', max_length=30, unique=True)),
                ('direccion', models.CharField(help_text='Dirección', max_length=60, unique=True)),
                ('celular', models.CharField(blank=True, max_length=20, null=True)),
                ('correo', models.EmailField(max_length=250)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Repartidores',
            },
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('nombre', models.CharField(help_text='Nombre de la Ruta', max_length=60, unique=True)),
                ('descripcion', models.CharField(help_text='Descripción de la Ruta', max_length=60, unique=True)),
                ('repartidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fac.repartidor')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Rutas',
            },
        ),
        migrations.CreateModel(
            name='FacturaEnc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('sub_total', models.FloatField(default=0)),
                ('descuento', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fac.cliente')),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Encabezado Factura',
                'verbose_name_plural': 'Encabezado Facturas',
                'permissions': [('sup_caja_facturaenc', 'Permisos de Supervisor de Caja Encabezado')],
            },
        ),
        migrations.CreateModel(
            name='FacturaDet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('cantidad', models.BigIntegerField(default=0)),
                ('precio', models.FloatField(default=0)),
                ('sub_total', models.FloatField(default=0)),
                ('descuento', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fac.facturaenc')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.producto')),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Detalle Factura',
                'verbose_name_plural': 'Detalles Facturas',
                'permissions': [('sup_caja_facturadet', 'Permisos de Supervisor de Caja Detalle')],
            },
        ),
        migrations.AddField(
            model_name='cliente',
            name='ruta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fac.ruta'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
