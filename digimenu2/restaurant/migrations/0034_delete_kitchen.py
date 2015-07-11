# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0033_auto_20150708_0917'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Kitchen',
        ),
    ]
