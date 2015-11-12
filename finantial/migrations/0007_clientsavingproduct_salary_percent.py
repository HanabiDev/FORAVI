# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finantial', '0006_auto_20151111_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientsavingproduct',
            name='salary_percent',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
    ]
