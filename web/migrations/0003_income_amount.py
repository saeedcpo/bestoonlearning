# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-22 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_income'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='amount',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
