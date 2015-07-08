# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0027_auto_20150706_0629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='item_name',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='menu_item',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Cartitem',
        ),
        migrations.DeleteModel(
            name='Userprofile',
        ),
    ]
