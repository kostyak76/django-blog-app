# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 14:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161012_1134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='category_id',
            new_name='category',
        ),
    ]
