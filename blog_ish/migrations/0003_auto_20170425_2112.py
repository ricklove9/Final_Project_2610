# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-25 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_ish', '0002_auto_20170425_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='name_text',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
