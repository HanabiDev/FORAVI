# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0003_auto_20150909_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('message', redactor.fields.RedactorField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True, verbose_name='Publicado')),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'art\xedculo'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='published',
        ),
        migrations.AlterField(
            model_name='post',
            name='related_articles',
            field=models.ManyToManyField(related_name='related', verbose_name='Art\xedculos relacionados', to='cms.Post', blank=True),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.Content')),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='T\xedtulo')),
                ('file', models.FileField(upload_to=b'uploads/documents/', verbose_name='Archivo')),
            ],
            bases=('cms.content',),
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.ForeignKey(to='cms.Content'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default='', serialize=False, to='cms.Content'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='related_documents',
            field=models.ManyToManyField(related_name='docs', verbose_name='Documentos relacionados', to='cms.Document', blank=True),
        ),
    ]
