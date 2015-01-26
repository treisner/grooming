# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_appointmentdetail_do_it'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='gcalid',
            field=models.CharField(unique=True, max_length=255),
            preserve_default=True,
        ),
    ]
