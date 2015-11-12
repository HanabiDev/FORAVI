# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finantial', '0003_auto_20151111_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finantialproduct',
            name='name',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
