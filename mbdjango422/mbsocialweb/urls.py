"""
URL configuration for mbsocialweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.conf import settings
from core.views import robots_txt
# from django.conf.urls import handler404

from blog.sitemaps import PostSitemap, StaticViewSitemap

sitemaps = {"posts": PostSitemap, "static": StaticViewSitemap}

urlpatterns = [
    # Path ADMIN
    path("admin/", admin.site.urls),
    # Path SITEMAP
    path(
        "sitemap.xml/",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    # path CKEDITOR
    path("ckeditor/", include("ckeditor_uploader.urls")),
    # path Robots
    path("robots.txt/", robots_txt),
    # Path CORE
    path("", include("core.urls")),
    # Path SOCIAL MEDIA
    path("social-media/", include("socialmedia.urls", namespace="social-media")),
    # Path MARKETING DIGITAL
    path("marketing-online/", include("marketing.urls", namespace="marketing-online")),
    # Path DISEÑO WEB
    path("diseno-web/", include("webdesign.urls", namespace="web-design")),
    # Path DISEÑO GRAFICO
    path("diseno-grafico/", include("graphicdesign.urls", namespace="graphic-design")),
    # Path CONTACTO
    path("contacto/", include("contact.urls", namespace="contact")),
    # Path NOSOTROS
    path("nosotros/", include("about.urls", namespace="about")),
    # Path BLOG
    path("blog/", include("blog.urls", namespace="blog")),
    # Path PAGE
    path("pagina/", include("page.urls", namespace="pagina")),
    # Path PORTFOLIO
    path("portafolio/", include("portfolio.urls", namespace="portfolio")),
    # Path PWA
    path('', include('pwa.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]

# handler404 = "core.views.error_404_view"

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)