# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import customers.django_orm
import django_localflavor_us.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('gcalid', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('notes', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AppointmentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('appointment', models.ForeignKey(to='customers.Appointment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('breed', models.CharField(unique=True, max_length=30)),
                ('description', models.CharField(blank=True, max_length=60)),
                ('size', models.CharField(default='ANY', choices=[('XS', 'XS Less than 15lb'), ('SM', 'SM 15lb to 30lb'), ('MD', 'MD 30lb to 50lb'), ('LG', 'LG 50lb to 100lb'), ('XL', 'XL More that 100lb'), ('ANY', 'All sizes the same')], max_length=4)),
                ('hair', models.CharField(default='ANY', choices=[('LH', 'Long Hair'), ('SH', 'SHORT HAIR'), ('ANY', 'All sizes the same')], max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('phone_number', django_localflavor_us.models.PhoneNumberField(max_length=20)),
                ('caller_id_name', models.CharField(max_length=30)),
                ('rang_at', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CredentialsModel',
            fields=[
                ('id', models.ForeignKey(serialize=False, to=settings.AUTH_USER_MODEL, primary_key=True)),
                ('credential', customers.django_orm.CredentialsField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('home_phone', django_localflavor_us.models.PhoneNumberField(unique=True, max_length=20)),
                ('work_phone', django_localflavor_us.models.PhoneNumberField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=75)),
                ('veterinarian', models.CharField(blank=True, max_length=30)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('sex', models.CharField(default=None, choices=[('M', 'M'), ('F', 'F')], max_length=1)),
                ('birthday', models.DateField(blank=True)),
                ('vaccinated', models.NullBooleanField(default=False)),
                ('noisy', models.NullBooleanField(default=False)),
                ('bites', models.NullBooleanField(default=False)),
                ('shy', models.NullBooleanField(default=False)),
                ('soils_cage', models.NullBooleanField(default=False)),
                ('arthritic', models.NullBooleanField(default=False)),
                ('epileptic', models.NullBooleanField(default=False)),
                ('overweight', models.NullBooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
                ('breed', models.ForeignKey(to='customers.Breed', default=1)),
                ('owner', models.ForeignKey(to='customers.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('service', models.CharField(unique=True, max_length=30)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('description', models.TextField(blank=True)),
                ('size', models.CharField(default='ANY', choices=[('XS', 'XS Less than 15lb'), ('SM', 'SM 15lb to 30lb'), ('MD', 'MD 30lb to 50lb'), ('LG', 'LG 50lb to 100lb'), ('XL', 'XL More that 100lb'), ('ANY', 'All sizes the same')], max_length=4)),
                ('hair', models.CharField(default='ANY', choices=[('LH', 'Long Hair'), ('SH', 'SHORT HAIR'), ('ANY', 'All sizes the same')], max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='call',
            name='customer',
            field=models.ForeignKey(to='customers.Customer', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointmentdetail',
            name='service',
            field=models.ForeignKey(to='customers.Service'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='appointmentdetail',
            unique_together=set([('appointment', 'service')]),
        ),
        migrations.AddField(
            model_name='appointment',
            name='pet',
            field=models.ForeignKey(to='customers.Pet'),
            preserve_default=True,
        ),
    ]
