# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20150108_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentdetail',
            name='do_it',
            field=models.NullBooleanField(default=False),
            preserve_default=True,
        ),
    ]
