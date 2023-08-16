from django.urls import path
from . import views

app_name = 'marketing'

urlpatterns = [
    # Path MARKETING DIGITAL
    path('google-ads/', views.ads, name='ads'),
    path('email-marketing/', views.emailMarketing, name='email-marketing'),
    path('publicidad-redes-sociales/', views.socialAds, name='social-ads'),
    path('posicionamiento-seo/', views.seo, name='seo'),
    path('google-my-business/', views.business, name='google-business'),
    path('analitica-web/', views.analiticWeb, name='analitic-web'),
]
