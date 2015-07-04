# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0017_auto_20150704_1109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='cuisine_name',
            new_name='cuisine_id',
        ),
        migrations.AlterField(
            model_name='cuisine',
            name='cuisine_id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='cuisine',
            name='cuisine_name',
            field=models.CharField(max_length=200),
        ),
    ]
