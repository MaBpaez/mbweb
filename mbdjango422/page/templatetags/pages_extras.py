from django import template
from django.shortcuts import get_object_or_404
from django.core.cache import cache

from page.models import Page

register = template.Library()


@register.simple_tag
def get_page_list():
    pages = cache.get("pages")
    if not pages:
        pages = Page.objects.all()
        cache.set("pages", pages, 60 * 15)

    return pages


@register.simple_tag
def get_page_privacy():
    page_privacy = cache.get('page_privacy')
    if not page_privacy:
        page_privacy = get_object_or_404(Page, id=2)
        cache.set('page_privacy', page_privacy, 60 * 15)

    return page_privacy
