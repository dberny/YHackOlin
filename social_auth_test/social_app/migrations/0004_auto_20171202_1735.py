# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 17:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0003_creator_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creator',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
    ]