from django import template
import locale
locale.setlocale(locale.LC_ALL, '')
register = template.Library()


@register.filter()
def currency(value):
    return locale.currency(value, grouping=True)

@register.filter
def substract(remaining, percent):

    remaining_percent = 100 - percent

    paid_money = (remaining * percent)/remaining_percent
    return  paid_money
