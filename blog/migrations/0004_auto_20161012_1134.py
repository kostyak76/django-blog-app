# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 14:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20161010_0951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='post_id',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='author_id',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='category_id',
        ),
    ]
