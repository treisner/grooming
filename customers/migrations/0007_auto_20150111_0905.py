# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_auto_20150110_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='todo',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='total',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=5),
            preserve_default=False,
        ),
    ]
