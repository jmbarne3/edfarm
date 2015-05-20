# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0003_bundle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='name_override',
        ),
        migrations.RemoveField(
            model_name='product',
            name='produce',
        ),
        migrations.RemoveField(
            model_name='product',
            name='unit_count',
        ),
        migrations.RemoveField(
            model_name='product',
            name='unit_type',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='Decription'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='./image-path', upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='name', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='plural_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Produce',
        ),
    ]
