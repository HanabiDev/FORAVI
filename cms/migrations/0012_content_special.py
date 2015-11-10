# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_document_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='special',
            field=models.BooleanField(default=False),
        ),
    ]
