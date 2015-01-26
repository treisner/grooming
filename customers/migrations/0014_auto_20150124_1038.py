# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0013_auto_20150123_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='picture',
            field=models.ImageField(upload_to='/media/customers/', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=15, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=15, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pet',
            name='sex',
            field=models.CharField(max_length=1, blank=True, default=None, choices=[('M', 'M'), ('F', 'F')]),
            preserve_default=True,
        ),
    ]
