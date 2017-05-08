# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message_board_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThreadList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ThreadListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thread_view', to='message_board_app.Thread')),
            ],
        ),
    ]
