# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-15 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body_sign', '0003_bodysignal_is_critical'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodysignal',
            name='is_critical',
            field=models.BooleanField(),
        ),
    ]