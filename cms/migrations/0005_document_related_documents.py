# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20150910_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='related_documents',
            field=models.ManyToManyField(related_name='related', verbose_name='Documentos relacionados', to='cms.Document', blank=True),
        ),
    ]
