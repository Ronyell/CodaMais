# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 11:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20170409_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2017, 4, 18)),
        ),
    ]