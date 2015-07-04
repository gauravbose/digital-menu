# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0021_auto_20150704_1154'),
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
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='table_no',
        ),
        migrations.DeleteModel(
            name='Table',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default='user', to='restaurant.Userprofile'),
            preserve_default=False,
        ),
    ]
