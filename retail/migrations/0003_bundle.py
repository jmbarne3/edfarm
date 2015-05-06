# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0002_auto_20150505_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=b'')),
                ('products', models.ManyToManyField(to='retail.Product')),
                ('sales', models.ManyToManyField(to='retail.Sale')),
            ],
        ),
    ]
