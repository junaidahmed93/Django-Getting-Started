# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 05:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_auto_20171121_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='assignee',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='reporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
