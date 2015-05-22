# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0007_auto_20150521_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='sales',
            field=models.ManyToManyField(to='retail.Sale', null=True, blank=True),
        ),
    ]
