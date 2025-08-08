from django import template

register = template.Library()

@register.filter(name='replace_spaces_with_underscores')
def replace_spaces_with_underscores(value):
    return value.replace(' ', '_')
