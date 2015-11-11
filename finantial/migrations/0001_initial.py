# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
        ('auth', '0008_auto_20150920_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('dni', models.CharField(max_length=30, verbose_name=b'Documento')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('backend.siteuser',),
        ),
        migrations.CreateModel(
            name='ClientCreditProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('promisory_note', models.CharField(max_length=30)),
                ('quota', models.DecimalField(max_digits=8, decimal_places=2)),
                ('amount', models.DecimalField(max_digits=9, decimal_places=2)),
                ('amortized_amount', models.DecimalField(max_digits=9, decimal_places=2)),
                ('amortized_percent', models.DecimalField(max_digits=3, decimal_places=2)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('client', models.ForeignKey(to='finantial.Client')),
            ],
        ),
        migrations.CreateModel(
            name='ClientSavingProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('savings_total', models.DecimalField(max_digits=9, decimal_places=2)),
                ('quota', models.DecimalField(max_digits=8, decimal_places=2)),
                ('client', models.ForeignKey(to='finantial.Client')),
            ],
        ),
        migrations.CreateModel(
            name='FinantialProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CreditLine',
            fields=[
                ('finantialproduct_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='finantial.FinantialProduct')),
                ('interest_rate', models.DecimalField(max_digits=3, decimal_places=1)),
            ],
            bases=('finantial.finantialproduct',),
        ),
        migrations.CreateModel(
            name='SavingLine',
            fields=[
                ('finantialproduct_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='finantial.FinantialProduct')),
                ('quota_base', models.DecimalField(max_digits=2, decimal_places=2)),
            ],
            bases=('finantial.finantialproduct',),
        ),
        migrations.AddField(
            model_name='clientsavingproduct',
            name='saving_line',
            field=models.ForeignKey(to='finantial.SavingLine'),
        ),
        migrations.AddField(
            model_name='clientcreditproduct',
            name='credit_line',
            field=models.ForeignKey(to='finantial.CreditLine'),
        ),
    ]
