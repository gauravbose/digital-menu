# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0035_kitchen'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitchen',
            name='orderid',
            field=models.CharField(default='id', max_length=200),
            preserve_default=False,
        ),
    ]
