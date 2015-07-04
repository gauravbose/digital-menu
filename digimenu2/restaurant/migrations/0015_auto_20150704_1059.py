# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0014_cuisine_cuisine_id'),
    ]

    operations = [
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
