# Generated by Django 4.1.1 on 2022-09-08 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='segmento',
            field=models.CharField(choices=[('Corporativo/Empresarial/Mayorista', 'Corporativo-Empresarial-Mayorista'), ('Natural/Detail/Minorista', 'Natural-Detail-Minorista'), ('Institucional/Público/Fundaciones', 'Institucional-Público-Fundaciones'), ('Tienda/Minimercado/Negocio', 'Tienda-Minimercado-Negocio')], default='Natural/Detail/Minorista', max_length=60),
        ),
    ]