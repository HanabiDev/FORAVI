# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_content_special'),
        ('admin', '0001_initial'),
        ('finantial', '0002_auto_20151111_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='user_ptr',
        ),
        migrations.AlterField(
            model_name='clientcreditproduct',
            name='client',
            field=models.ForeignKey(to='backend.SiteUser'),
        ),
        migrations.AlterField(
            model_name='clientsavingproduct',
            name='client',
            field=models.ForeignKey(to='backend.SiteUser'),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]
