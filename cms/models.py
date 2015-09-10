#encoding: utf-8
from django.db import models
from django.template.defaultfilters import slugify
from redactor.fields import RedactorField

class Post(models.Model):
    slug = models.SlugField(unique=True, blank=True)
    title = models.CharField(max_length=100, verbose_name=u'Título', unique=True)
    date = models.DateTimeField(auto_now=True)
    abstract = RedactorField(verbose_name=u'Resumen')
    content = RedactorField(verbose_name=u'Contenido')
    published = models.BooleanField(default=True, verbose_name=u'Publicado')
    related_articles = models.ManyToManyField('Post', verbose_name=u'Artículos relacionados', related_name='related', blank=True)

    class Meta:
        verbose_name = u'artículo'
    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)