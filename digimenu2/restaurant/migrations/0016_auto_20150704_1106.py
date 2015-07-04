# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0015_auto_20150704_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='cuisine_name',
            new_name='cuisine_id',
        ),
    ]
