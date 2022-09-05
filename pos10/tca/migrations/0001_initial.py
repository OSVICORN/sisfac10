# Generated by Django 4.1.1 on 2022-09-05 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cmp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NdebEnc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('fecha_nota', models.DateField(blank=True, null=True)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('total', models.FloatField(default=0)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmp.proveedor')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Encabezado Nota Débito',
                'verbose_name_plural': 'Encabezado Notas Débito',
            },
        ),
        migrations.CreateModel(
            name='NdebDet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('total', models.FloatField(default=0)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmp.comprasenc')),
                ('nota_debito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tca.ndebenc')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
