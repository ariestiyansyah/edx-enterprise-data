# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-30 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enterpriseenrollment',
            old_name='enterprise_sso_user_id',
            new_name='enterprise_sso_uid',
        ),
        migrations.AddField(
            model_name='enterpriseenrollment',
            name='enterprise_sso_site_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
