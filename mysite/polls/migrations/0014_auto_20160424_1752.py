# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 09:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_solution_solutiontype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='ptype',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='polls.SolutionType', verbose_name='\u7c7b\u578b'),
        ),
    ]