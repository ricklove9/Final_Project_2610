# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-25 17:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_ish', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='blog_text',
            new_name='post_text',
        ),
    ]
