# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-25 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0006_remove_detallereserva_codigo_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallereserva',
            name='costo_implemento',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detallereserva',
            name='fecha_fin',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detallereserva',
            name='fecha_inicio',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
