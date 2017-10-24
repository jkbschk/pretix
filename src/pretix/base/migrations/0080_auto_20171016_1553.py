# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0079_auto_20171010_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartposition',
            name='cart_id',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Cart ID (e.g. session key)'),
        ),
    ]