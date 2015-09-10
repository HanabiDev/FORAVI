# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=50, verbose_name='T\xedtulo')),
                ('date', models.DateTimeField(auto_now=True)),
                ('abstract', redactor.fields.RedactorField(verbose_name='Resumen')),
                ('content', redactor.fields.RedactorField(verbose_name='Contenido')),
                ('published', models.BooleanField(default=True, verbose_name='Publicado')),
                ('related_articles', models.ManyToManyField(related_name='related', null=True, verbose_name='Art\xedculos relacionados', to='cms.Post', blank=True)),
            ],
        ),
    ]
