# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 11:58
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtilte', models.CharField(max_length=500)),
                ('autor', models.CharField(max_length=200)),
                ('description', redactor.fields.RedactorField(verbose_name='Text')),
                ('dateTopic', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]