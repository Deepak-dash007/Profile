from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()
register = template.Library()
@register.filter(name='split')
@stringfilter
def split(value,arg):
	return value.split(arg)


@register.filter(name='format')

def format(value,arg):
	return value.strftime(arg)