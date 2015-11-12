# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finantial', '0008_remove_clientsavingproduct_salary_percent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditline',
            name='finantialproduct_ptr',
        ),
        migrations.AddField(
            model_name='clientsavingproduct',
            name='salary_percent',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CreditLine',
        ),
        migrations.CreateModel(
            name='CreditLine',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('finantial.finantialproduct',),
        ),
    ]
