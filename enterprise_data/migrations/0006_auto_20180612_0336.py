# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-12 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise_data', '0005_auto_20180524_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterpriseenrollment',
            name='last_activity_timestamp',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='enterpriseenrollment',
            name='user_country_code',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
