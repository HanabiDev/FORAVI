# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finantial', '0005_auto_20151111_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcreditproduct',
            name='amortized_percent',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='clientcreditproduct',
            name='amount',
            field=models.DecimalField(max_digits=11, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='clientcreditproduct',
            name='quota',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='clientcreditproduct',
            name='remaining_amount',
            field=models.DecimalField(max_digits=11, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='clientsavingproduct',
            name='quota',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='clientsavingproduct',
            name='savings_total',
            field=models.DecimalField(max_digits=11, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='creditline',
            name='interest_rate',
            field=models.DecimalField(max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='savingline',
            name='quota_base',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
    ]
