# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 15:29
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('legislator', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('uid', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('former_names', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=None, null=True, size=None)),
                ('birth', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('ad', models.IntegerField(db_index=True)),
                ('number', models.IntegerField(blank=True, db_index=True, null=True)),
                ('priority', models.IntegerField(blank=True, db_index=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('party', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('constituency', models.IntegerField(db_index=True)),
                ('county', models.CharField(db_index=True, max_length=100)),
                ('district', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('votes', models.IntegerField(blank=True, null=True)),
                ('votes_percentage', models.CharField(blank=True, max_length=100, null=True)),
                ('elected', models.NullBooleanField(db_index=True)),
                ('contact_details', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('education', models.TextField(blank=True, null=True)),
                ('experience', models.TextField(blank=True, null=True)),
                ('remark', models.TextField(blank=True, null=True)),
                ('image', models.URLField(blank=True, null=True)),
                ('links', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('platform', models.TextField(blank=True, null=True)),
                ('politicalcontributions', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('councilor', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('cec_data', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.Candidates')),
                ('latest_term', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='legislator.LegislatorDetail')),
                ('legislator', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='elected_candidate', to='legislator.LegislatorDetail')),
            ],
        ),
        migrations.AlterIndexTogether(
            name='terms',
            index_together=set([('ad', 'county', 'constituency')]),
        ),
    ]
