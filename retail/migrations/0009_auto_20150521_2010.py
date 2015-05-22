# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0008_auto_20150521_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='sales',
            field=models.ManyToManyField(to='retail.Sale', blank=True),
        ),
    ]
