# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20160424_0843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producttype',
            old_name='img1',
            new_name='img',
        ),
        migrations.AlterField(
            model_name='product',
            name='ptype',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='polls.ProductType', verbose_name='\u7c7b\u578b'),
        ),
    ]
