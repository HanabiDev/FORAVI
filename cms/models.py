#encoding: utf-8
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from redactor.fields import RedactorField

class Content(models.Model):
    date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True, verbose_name=u'Publicado')
    special = models.BooleanField(default=False)

class Document(Content):
    slug = models.SlugField(unique=True, blank=True)
    name = models.CharField(max_length=100, verbose_name=u'Nombre', unique=True)
    description = RedactorField(verbose_name=u'Descripción')
    file = models.FileField(upload_to='media/uploads/documents/', verbose_name=u'Archivo')
    related_documents = models.ManyToManyField('Document', verbose_name=u'Documentos relacionados', related_name='docs', blank=True)
    related_articles = models.ManyToManyField('Post', verbose_name=u'Artículos relacionados', related_name='posts', blank=True)

    class Meta:
        verbose_name = u'documento'

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Document, self).save(*args, **kwargs)


class Post(Content):
    slug = models.SlugField(unique=True, blank=True)
    title = models.CharField(max_length=100, verbose_name=u'Título', unique=True)
    abstract = RedactorField(verbose_name=u'Resumen')
    content = RedactorField(verbose_name=u'Contenido')
    related_articles = models.ManyToManyField('Post', verbose_name=u'Artículos relacionados', related_name='related_posts', blank=True)
    related_documents = models.ManyToManyField('Document', verbose_name=u'Documentos relacionados', related_name='related_docs', blank=True)
    class Meta:
        verbose_name = u'artículo'
    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    content = models.ForeignKey('Content')
    author = models.ForeignKey(User)
    message = models.TextField()


