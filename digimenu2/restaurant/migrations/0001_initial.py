# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.IntegerField(serialize=False, primary_key=True)),
                ('item_name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cartlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('cuisine_name', models.CharField(max_length=200, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_item', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('cuisine_name', models.ForeignKey(to='restaurant.Cuisine')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('table_no', models.IntegerField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('phone_no', models.IntegerField()),
                ('password', models.CharField(max_length=7, serialize=False, primary_key=True)),
                ('bill_id', models.IntegerField()),
                ('table_no', models.ForeignKey(to='restaurant.Table')),
            ],
        ),
        migrations.AddField(
            model_name='cartlist',
            name='bill_id',
            field=models.ForeignKey(to='restaurant.User'),
        ),
        migrations.AddField(
            model_name='cartlist',
            name='cart_id',
            field=models.ForeignKey(to='restaurant.Cart'),
        ),
    ]
