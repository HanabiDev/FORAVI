# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finantial', '0004_auto_20151111_1940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientcreditproduct',
            old_name='amortized_amount',
            new_name='remaining_amount',
        ),
        migrations.AddField(
            model_name='clientcreditproduct',
            name='remaining_payments',
            field=models.IntegerField(default=999),
            preserve_default=False,
        ),
    ]
