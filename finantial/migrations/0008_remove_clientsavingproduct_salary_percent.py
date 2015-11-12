# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finantial', '0007_clientsavingproduct_salary_percent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientsavingproduct',
            name='salary_percent',
        ),
    ]
