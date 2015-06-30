# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_auto_20150629_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartlist',
            name='bill_id',
        ),
        migrations.RemoveField(
            model_name='cartlist',
            name='cart_id',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Cartlist',
        ),
    ]
