# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0004_auto_20150520_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('regular_price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('sales', models.ManyToManyField(to='retail.Sale', blank=True)),
                ('unit_designation', models.ForeignKey(to='retail.UnitType')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='regular_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sales',
        ),
        migrations.AddField(
            model_name='product',
            name='prices',
            field=models.ManyToManyField(to='retail.Price'),
        ),
    ]
