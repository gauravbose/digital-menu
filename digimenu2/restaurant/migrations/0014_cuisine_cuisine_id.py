# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0013_auto_20150703_0608'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuisine',
            name='cuisine_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
