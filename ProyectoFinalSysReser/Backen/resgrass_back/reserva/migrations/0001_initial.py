# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-25 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogo', '0006_auto_20170625_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleReserva',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('codigo_reserva', models.CharField(max_length=10)),
                ('costo', models.FloatField()),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('catalogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Catalogo')),
            ],
            options={
                'verbose_name_plural': 'DetalleReservas',
                'verbose_name': 'DetalleReserva',
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Persona')),
            ],
            options={
                'verbose_name_plural': 'Reservas',
                'verbose_name': 'Reserva',
            },
        ),
        migrations.AddField(
            model_name='detallereserva',
            name='reserva',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reserva.Reserva'),
        ),
    ]
