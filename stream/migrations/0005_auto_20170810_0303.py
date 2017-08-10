# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 01:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0004_auto_20170810_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitch',
            name='facebook_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='twitch',
            name='youtube_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
