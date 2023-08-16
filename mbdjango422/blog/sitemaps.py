from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Post


class PostSitemap(Sitemap):

    changefre = 'weekly'
    priority = 0.9
    protocol = 'https'

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.publish

class StaticViewSitemap(Sitemap):

    changefre = 'weekly'
    priority = 0.9
    protocol = 'https'

    def items(self):
        return [
            'home',
            'socialmedia:fbshop',
            'socialmedia:appsfb',
            'socialmedia:smcontent',
            'socialmedia:creation-network',
            'marketing:ads',
            'marketing:email-marketing',
            'marketing:social-ads',
            'marketing:seo',
            'marketing:google-business',
            'marketing:analitic-web',
            'webdesign:custom-web',
            'webdesign:hosting',
            'webdesign:landing',
            'webdesign:custom-blog',
            'webdesign:portfolio',
            'webdesign:web-maintenance',
            'graphicdesign:corporate-image',
            'graphicdesign:logotipo',
            'contact:contacto',
            'about:us',
            'portfolio:portafolio',
        ]

    def location(self, item):
        return reverse(item)
