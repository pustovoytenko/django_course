# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 10:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0003_auto_20170412_2019'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entry',
        ),
    ]