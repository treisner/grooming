# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0011_auto_20150119_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='customer',
            field=models.ForeignKey(to='customers.Customer'),
            preserve_default=True,
        ),
    ]
