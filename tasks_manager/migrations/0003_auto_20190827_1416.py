# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-27 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_manager', '0002_auto_20190827_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasksmanager',
            name='due_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
