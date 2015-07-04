# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0016_auto_20150704_1106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='cuisine_id',
            new_name='cuisine_name',
        ),
        migrations.AlterField(
            model_name='cuisine',
            name='cuisine_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cuisine',
            name='cuisine_name',
            field=models.CharField(max_length=200, serialize=False, primary_key=True),
        ),
    ]
