# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 05:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message_board_app', '0002_threadlist_threadlistitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ThreadList',
        ),
        migrations.RemoveField(
            model_name='threadlistitem',
            name='item',
        ),
        migrations.DeleteModel(
            name='ThreadListItem',
        ),
    ]
