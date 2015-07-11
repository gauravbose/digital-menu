# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0032_kitchen_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitchen',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
