# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-01 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0028_auto_20160901_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='year',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
