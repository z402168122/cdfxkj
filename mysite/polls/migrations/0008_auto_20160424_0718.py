# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 23:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20160424_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='create_time',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 4, 23, 23, 18, 0, 560000, tzinfo=utc), verbose_name='\u521b\u5efa\u65f6\u95f4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='detail',
            field=models.CharField(default='', max_length=60, verbose_name='\u7b80\u5355\u4ecb\u7ecd'),
        ),
        migrations.AlterField(
            model_name='abouts',
            name='ptype',
            field=models.IntegerField(choices=[(0, '\u6700\u65b0\u8d44\u8baf'), (1, '\u516c\u53f8\u4ecb\u7ecd')], default=0, verbose_name='\u7c7b\u578b'),
        ),
    ]
