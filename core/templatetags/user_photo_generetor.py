from django.template import Library

register = Library()

@register.inclusion_tag('templatetags/userPhoto.html')
def user_photo_generetor(user):
    return {'letter' : user.username.upper()[0]}