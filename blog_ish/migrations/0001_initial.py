# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-23 22:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_text', models.CharField(max_length=500)),
                ('date_published', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=50)),
                ('date_signup', models.DateTimeField(verbose_name='date sign up')),
                ('password_text', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_ish.User'),
        ),
    ]
