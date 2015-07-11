# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0031_auto_20150708_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitchen',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
