# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuisine',
            name='image_path',
            field=models.CharField(default='restaurant', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=b'images', verbose_name=b'My Photo'),
        ),
    ]
