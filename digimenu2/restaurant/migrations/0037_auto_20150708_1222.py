# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0036_kitchen_orderid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitchen',
            name='status',
            field=models.CharField(default=b'Received', max_length=20, choices=[(b'Received', b'recieved'), (b'Preparing', b'preparing'), (b'Prepared', b'prepared'), (b'Delivered', b'delivered')]),
        ),
    ]
