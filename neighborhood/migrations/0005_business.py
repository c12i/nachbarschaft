# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-12-02 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '0004_auto_20191202_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=144)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=144)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to='neighborhood.Group')),
            ],
        ),
    ]
