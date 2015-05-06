# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produce',
            options={'verbose_name_plural': 'Produce'},
        ),
        migrations.AddField(
            model_name='produce',
            name='plural_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
