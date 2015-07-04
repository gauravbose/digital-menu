# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0023_auto_20150704_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='item_name',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='menu_item',
        ),
        migrations.DeleteModel(
            name='Cartitem',
        ),
    ]
