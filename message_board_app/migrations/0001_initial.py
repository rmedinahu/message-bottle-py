# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 19:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('createdby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_responses', to=settings.AUTH_USER_MODEL)),
                ('parent_response', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='message_board_app.Response')),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('createdby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ThreadUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField()),
                ('bio', models.TextField()),
                ('thread_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='response',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='message_board_app.Thread'),
        ),
    ]
