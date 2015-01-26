# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_auto_20150111_0905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breed',
            name='hair',
        ),
        migrations.RemoveField(
            model_name='service',
            name='hair',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='todo',
            field=models.CharField(max_length=64, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='service',
            unique_together=set([('service', 'size')]),
        ),
    ]
