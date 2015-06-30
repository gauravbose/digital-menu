# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_menu_image_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_id',
        ),
        migrations.AddField(
            model_name='cart',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default='a', serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
