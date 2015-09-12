# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_document_related_documents'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'documento'},
        ),
        migrations.AlterField(
            model_name='document',
            name='name',
            field=models.CharField(unique=True, max_length=100, verbose_name='Nombre'),
        ),
    ]
