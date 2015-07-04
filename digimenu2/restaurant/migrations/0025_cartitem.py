# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0024_auto_20150704_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartitem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.ForeignKey(to='restaurant.Cart')),
                ('menu_item', models.ForeignKey(to='restaurant.Menu')),
            ],
        ),
    ]
