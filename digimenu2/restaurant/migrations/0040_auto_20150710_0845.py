# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0039_auto_20150709_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitchen',
            name='status',
            field=models.CharField(default=b'Nochange', max_length=20, choices=[(b'Nochange', b'no change'), (b'Received', b'recieved'), (b'Preparing', b'preparing'), (b'Prepared', b'prepared'), (b'Delivered', b'delivered'), (b'Notavailable', b'not available')]),
        ),
    ]
