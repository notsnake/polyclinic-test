# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 09:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'verbose_name': 'doctor_verbose_name', 'verbose_name_plural': 'doctor_verbose_name_plural'},
        ),
        migrations.AlterModelOptions(
            name='doctorrecord',
            options={'verbose_name': 'record_verbose_name', 'verbose_name_plural': 'record_verbose_name_plural'},
        ),
        migrations.AlterField(
            model_name='doctor',
            name='fio',
            field=models.CharField(max_length=150, verbose_name='doctor_fio'),
        ),
        migrations.AlterField(
            model_name='doctorrecord',
            name='date_record',
            field=models.DateTimeField(verbose_name='date_record'),
        ),
        migrations.AlterField(
            model_name='doctorrecord',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.Doctor', verbose_name='doctor_fio'),
        ),
        migrations.AlterField(
            model_name='doctorrecord',
            name='patient_fio',
            field=models.CharField(max_length=150, verbose_name='patient_fio'),
        ),
    ]
