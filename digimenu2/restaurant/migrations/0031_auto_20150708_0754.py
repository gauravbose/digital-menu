# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0030_kitchen_usertable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitchen',
            name='menu_item',
            field=models.CharField(max_length=200),
        ),
    ]
