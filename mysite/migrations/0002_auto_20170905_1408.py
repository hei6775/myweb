# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 06:08
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bozhu',
            name='body',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='\u6587\u7ae0\u6b63\u6587'),
        ),
    ]
