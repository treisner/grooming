# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0010_auto_20150117_1106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='breed',
            options={'ordering': ['breed']},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['service', '-price']},
        ),
        migrations.AlterField(
            model_name='call',
            name='customer',
            field=models.ForeignKey(to='customers.Customer', to_field='home_phone'),
            preserve_default=True,
        ),
    ]
