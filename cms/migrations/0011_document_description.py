# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_auto_20150930_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='description',
            field=redactor.fields.RedactorField(default='Doc', verbose_name='Descripci\xf3n'),
            preserve_default=False,
        ),
    ]
