# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_printer_isdefaultprinter'),
    ]

    operations = [
        migrations.AddField(
            model_name='printer',
            name='description',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
