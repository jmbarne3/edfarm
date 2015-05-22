# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0009_auto_20150521_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='prices',
        ),
        migrations.AddField(
            model_name='price',
            name='product',
            field=models.ForeignKey(related_name='prices', default=1, to='retail.Product'),
            preserve_default=False,
        ),
    ]
