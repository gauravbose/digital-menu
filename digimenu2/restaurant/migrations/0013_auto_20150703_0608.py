# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0012_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='cuisine',
        ),
        migrations.DeleteModel(
            name='image',
        ),
    ]
