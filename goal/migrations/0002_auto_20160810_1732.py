# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-10 12:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='stopdate',
            new_name='completedate',
        ),
        migrations.RemoveField(
            model_name='task',
            name='treevalue',
        ),
    ]