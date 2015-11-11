# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finantial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='dni',
            field=models.CharField(unique=True, max_length=30, verbose_name=b'Documento'),
        ),
    ]
