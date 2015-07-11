# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0029_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('table', models.IntegerField()),
                ('status', models.CharField(default=b'RC', max_length=2, choices=[(b'RC', b'recieved'), (b'PG', b'preparing'), (b'PD', b'prepared'), (b'DD', b'delivered')])),
                ('menu_item', models.ForeignKey(to='restaurant.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Usertable',
            fields=[
                ('table_no', models.IntegerField(serialize=False, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
