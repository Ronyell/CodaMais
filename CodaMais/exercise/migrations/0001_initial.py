# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-27 23:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import redactor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.PositiveIntegerField(choices=[(1, 'Básico'), (2, 'Intermediário'), (3, 'Avançado')])),
                ('statement_question', redactor.fields.RedactorField(verbose_name='Text')),
                ('score', models.PositiveIntegerField()),
                ('deprecated', models.PositiveIntegerField(choices=[(0, 'Não'), (1, 'Sim')])),
            ],
        ),
        migrations.CreateModel(
            name='TestCaseExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_exercise', models.TextField(max_length=1000)),
                ('output_exercise', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='UserExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_submission', models.PositiveIntegerField(default=0)),
                ('code', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('time', models.CharField(default=0, max_length=10)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise.Exercise')),
            ],
        ),
    ]