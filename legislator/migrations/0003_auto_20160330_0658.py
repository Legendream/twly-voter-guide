# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 06:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legislator', '0002_legislator_identifiers'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together=set([('legislator', 'sitting', 'category')]),
        ),
    ]
