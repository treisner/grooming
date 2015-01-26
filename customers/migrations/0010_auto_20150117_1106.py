# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0009_auto_20150111_1503'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'ordering': ['when']},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AlterModelOptions(
            name='pet',
            options={'ordering': ['name', 'owner']},
        ),
        migrations.AlterField(
            model_name='breed',
            name='breed',
            field=models.CharField(unique=True, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='breed',
            name='description',
            field=models.CharField(blank=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=15),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=15),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pet',
            name='name',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='service',
            name='service',
            field=models.CharField(max_length=15),
            preserve_default=True,
        ),
    ]
