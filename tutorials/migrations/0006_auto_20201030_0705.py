# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-30 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0005_auto_20201030_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorials',
            name='tutorial_content',
            field=models.TextField(),
        ),
    ]
