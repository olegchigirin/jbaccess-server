# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jba_core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simplerecurringpattern',
            name='from_time',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='simplerecurringpattern',
            name='until_time',
            field=models.DurationField(),
        ),
    ]
