# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 21:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stream', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YouTube',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=23)),
                ('add_date', models.DateTimeField(verbose_name='date published')),
                ('video_id', models.CharField(max_length=23)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
