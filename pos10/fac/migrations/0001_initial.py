# Generated by Django 4.0 on 2022-07-23 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
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
            ],
            options={
                'verbose_name_plural': 'Clientes',
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
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
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
            ],
            options={
                'verbose_name': 'Detalle Factura',
                'verbose_name_plural': 'Detalles Facturas',
                'permissions': [('sup_caja_facturadet', 'Permisos de Supervisor de Caja Detalle')],
            },
        ),
    ]