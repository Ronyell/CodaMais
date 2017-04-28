# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-27 23:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exercise', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='userexercise',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='testcaseexercise',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_cases', to='exercise.Exercise'),
        ),
        migrations.AlterUniqueTogether(
            name='userexercise',
            unique_together=set([('user', 'exercise')]),
        ),
    ]