# Generated by Django 4.0.6 on 2022-07-27 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0002_repartidor'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruta',
            name='repartidor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fac.repartidor'),
        ),
    ]
