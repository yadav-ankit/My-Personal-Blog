# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 04:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20170311_0410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='draft',
        ),
        migrations.RemoveField(
            model_name='post',
            name='publish',
        ),
    ]
