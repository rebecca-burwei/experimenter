# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-27 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0002_experiment_experimentvariant'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='analysis',
            field=models.TextField(default=''),
        ),
    ]
