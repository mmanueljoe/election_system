from django import template
from election_app.models import Vote

register = template.Library()

from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, None)
