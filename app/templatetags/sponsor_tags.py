from django import template
from app.models import Sponsor

register = template.Library()

@register.simple_tag()
def get_sponsors():
    return Sponsor.objects.filter(active=True)