# Generated by Django 4.0 on 2022-07-23 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(help_text='Descripción de la Categoría', max_length=100, unique=True)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(help_text='Descripción de la Marca', max_length=100, unique=True)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'verbose_name_plural': 'Marca',
            },
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(help_text='Descripción de la Unidad Medida', max_length=100, unique=True)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'verbose_name_plural': 'Unidades de Medida',
            },
        ),
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(help_text='Descripción de la SubCategoría', max_length=100)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.categoria')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'verbose_name_plural': 'Sub Categorias',
                'unique_together': {('categoria', 'descripcion')},
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('codigo_barra', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('precio', models.FloatField(default=0)),
                ('existencia', models.IntegerField(default=0)),
                ('ultima_compra', models.DateField(blank=True, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.marca')),
                ('subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.subcategoria')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('unidad_medida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.unidadmedida')),
            ],
            options={
                'verbose_name_plural': 'Productos',
                'unique_together': {('codigo', 'codigo_barra')},
            },
        ),
    ]