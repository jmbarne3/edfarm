# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produce',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit_count', models.IntegerField()),
                ('name_override', models.CharField(max_length=255, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('regular_price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('produce', models.ForeignKey(to='retail.Produce')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sale_price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UnitType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('plural', models.CharField(max_length=255)),
                ('abbreviation', models.CharField(max_length=3)),
                ('abbreviation_plural', models.CharField(max_length=4)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='sales',
            field=models.ManyToManyField(to='retail.Sale'),
        ),
        migrations.AddField(
            model_name='product',
            name='unit_type',
            field=models.ForeignKey(to='retail.UnitType'),
        ),
    ]
