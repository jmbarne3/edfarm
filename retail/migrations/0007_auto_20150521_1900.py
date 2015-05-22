# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0006_auto_20150521_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='unit_designation',
            field=models.CharField(max_length=25),
        ),
    ]
