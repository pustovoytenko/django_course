# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 20:19
from __future__ import unicode_literals

from django.db import migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='body',
            field=redactor.fields.RedactorField(verbose_name='Text'),
        ),
    ]
