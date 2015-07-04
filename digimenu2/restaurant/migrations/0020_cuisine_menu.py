# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0019_auto_20150704_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('cuisine_id', models.IntegerField(serialize=False, primary_key=True)),
                ('cuisine_name', models.CharField(max_length=200)),
                ('image_path', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_item', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('image_path', models.CharField(max_length=100)),
                ('cuisine_id', models.ForeignKey(to='restaurant.Cuisine')),
            ],
        ),
    ]
