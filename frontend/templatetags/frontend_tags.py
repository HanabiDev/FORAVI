from django.utils.datetime_safe import datetime
from django import template
from cms.models import Post

register = template.Library()

@register.filter(name='get_years')
def get_years(number):
    years = range(datetime.now().year, (datetime.now().year + number))
    return years

@register.filter(name='get_months')
def get_months(actual_month):
    remaining_months = 12-actual_month
    years = range(datetime.now().month, (datetime.now().month + remaining_months))
    return years


@register.filter(name='get_last_posts')
def get_last_posts(chain):
    posts = Post.objects.filter(published=True).order_by('-date')[:5]
    return posts

