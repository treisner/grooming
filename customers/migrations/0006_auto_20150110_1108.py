# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20150109_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='time',
        ),
        migrations.AddField(
            model_name='appointment',
            name='when',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 10, 16, 8, 35, 237252, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
