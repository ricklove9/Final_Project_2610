# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-27 17:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_ish', '0005_remove_user_date_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=500)),
                ('date_published', models.DateTimeField(verbose_name='date published')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_ish.Post')),
            ],
        ),
    ]
