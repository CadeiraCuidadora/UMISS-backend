# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-15 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body_sign', '0004_auto_20170515_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodysignal',
            name='is_critical',
            field=models.BooleanField(default=False),
        ),
    ]