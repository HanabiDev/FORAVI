from django import template
from cms.models import Comment

register = template.Library()


@register.assignment_tag
def get_last_comments():
    comments = Comment.objects.all().order_by('date')[:10]
    print dir(comments[0].content)
    return comments