# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 05:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_auto_20171121_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='assignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quickstart', to=settings.AUTH_USER_MODEL),
        ),
    ]
