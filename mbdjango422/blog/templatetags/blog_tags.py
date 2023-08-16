from django import template
# from django.core.cache import cache

from blog.models import Category, Post


register = template.Library()


@register.inclusion_tag('blog/latest_categories.html')
def show_latest_categories(count=10):
    # latest_categories = cache.get('latest_categories')
    # if not latest_categories:
    latest_categories = Category.objects.all().order_by('name')[:count]
        # cache.set('latest_categories', latest_categories, 60 * 15)

    return {'latest_categories': latest_categories}


@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts(count=6):
    # latest_posts = cache.get('latest_posts')
    # if not latest_posts:
    latest_posts = Post.published.order_by('-publish')[:count]
        # cache.set('latest_posts', latest_posts, 60 * 15)

    return {'latest_posts': latest_posts}
