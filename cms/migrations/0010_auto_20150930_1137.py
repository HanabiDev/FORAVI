# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0009_document_related_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='related_documents',
            field=models.ManyToManyField(related_name='docs', verbose_name='Documentos relacionados', to='cms.Document', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='related_articles',
            field=models.ManyToManyField(related_name='related_posts', verbose_name='Art\xedculos relacionados', to='cms.Post', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='related_documents',
            field=models.ManyToManyField(related_name='related_docs', verbose_name='Documentos relacionados', to='cms.Document', blank=True),
        ),
    ]
