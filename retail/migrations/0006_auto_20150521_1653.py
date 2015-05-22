# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0005_auto_20150521_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prices',
            field=models.ManyToManyField(related_name='Product_prices', to='retail.Price'),
        ),
    ]
