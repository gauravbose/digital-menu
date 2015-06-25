# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20150623_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image_path',
            field=models.CharField(default='restaurant', max_length=100),
            preserve_default=False,
        ),
    ]
