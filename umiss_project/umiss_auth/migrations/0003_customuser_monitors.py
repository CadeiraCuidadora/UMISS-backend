# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-22 22:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('umiss_auth', '0002_customuser_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='monitors',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='monitors_users',
                to=settings.AUTH_USER_MODEL),
        ),
    ]
