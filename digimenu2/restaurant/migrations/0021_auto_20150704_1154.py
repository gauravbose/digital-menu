# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0020_cuisine_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuisine',
            name='cuisine_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
