# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20160903_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='jobid',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='priority',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='printer',
            name='deviceid',
            field=models.IntegerField(default=1),
        ),
    ]