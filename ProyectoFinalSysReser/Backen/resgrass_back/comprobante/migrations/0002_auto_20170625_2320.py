# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-25 23:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0009_auto_20170625_2210'),
        ('comprobante', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comprobante',
            name='detalle_reserva',
        ),
        migrations.AddField(
            model_name='comprobante',
            name='igv',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comprobante',
            name='precio_venta',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comprobante',
            name='reserva',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reserva.DetalleReserva'),
        ),
        migrations.AddField(
            model_name='comprobante',
            name='valor_venta',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
