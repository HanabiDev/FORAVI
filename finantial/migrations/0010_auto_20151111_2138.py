# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finantial', '0009_auto_20151111_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savingline',
            name='finantialproduct_ptr',
        ),
        migrations.DeleteModel(
            name='CreditLine',
        ),
        migrations.CreateModel(
            name='CreditLine',
            fields=[
                ('finantialproduct_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='finantial.FinantialProduct')),
                ('interest_rate', models.DecimalField(max_digits=4, decimal_places=1)),
            ],
            bases=('finantial.finantialproduct',),
        ),
        migrations.DeleteModel(
            name='SavingLine',
        ),
        migrations.CreateModel(
            name='SavingLine',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('finantial.finantialproduct',),
        ),
    ]
