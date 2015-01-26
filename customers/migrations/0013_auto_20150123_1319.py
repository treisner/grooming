# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0012_auto_20150119_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='breed',
            name='picture',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='breed',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
