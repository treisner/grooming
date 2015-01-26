# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_localflavor_us.models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='description',
            field=models.CharField(max_length=60),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='call',
            name='customer',
            field=models.ForeignKey(to='customers.Customer'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='notes',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='veterinarian',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='work_phone',
            field=django_localflavor_us.models.PhoneNumberField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pet',
            name='birthday',
            field=models.DateField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pet',
            name='breed',
            field=models.ForeignKey(to='customers.Breed', default=-1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pet',
            name='notes',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
