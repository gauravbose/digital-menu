# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0018_auto_20150704_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='cuisine_id',
        ),
        migrations.DeleteModel(
            name='Cuisine',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]
