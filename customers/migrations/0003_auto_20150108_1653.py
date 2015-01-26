# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_localflavor_us.models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20150108_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='notes',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='breed',
            name='description',
            field=models.CharField(blank=True, max_length=60),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='notes',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='veterinarian',
            field=models.CharField(blank=True, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='work_phone',
            field=django_localflavor_us.models.PhoneNumberField(blank=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pet',
            name='birthday',
            field=models.DateField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pet',
            name='notes',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='service',
            name='service',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='service',
            unique_together=set([('service', 'size', 'hair')]),
        ),
    ]
