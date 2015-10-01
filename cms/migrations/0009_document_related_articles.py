# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_auto_20150930_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='related_articles',
            field=models.ManyToManyField(related_name='posts', verbose_name='Art\xedculos relacionados', to='cms.Post', blank=True),
        ),
    ]
