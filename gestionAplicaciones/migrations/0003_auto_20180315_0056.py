# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-15 00:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionAplicaciones', '0002_auto_20180315_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aplicacion',
            name='url',
            field=models.URLField(max_length=50, unique=True, verbose_name='URL de la Aplicación'),
        ),
    ]