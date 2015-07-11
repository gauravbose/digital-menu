# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0034_delete_kitchen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('table', models.IntegerField()),
                ('menu_item', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(default=b'RC', max_length=2, choices=[(b'RC', b'recieved'), (b'PG', b'preparing'), (b'PD', b'prepared'), (b'DD', b'delivered')])),
            ],
        ),
    ]
