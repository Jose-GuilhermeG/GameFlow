from django.template import Library

register = Library()

@register.inclusion_tag('templatetags/pagination.html',takes_context=True)
def pagination(context):
    return context