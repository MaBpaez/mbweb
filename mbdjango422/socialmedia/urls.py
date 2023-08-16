from django.urls import path
from . import views

app_name = 'socialmedia'

urlpatterns = [
    # Path SOCIAL MEDIA
    path('tiendas-online-en-facebook-e-instagram/', views.fbshop, name='fbshop'),
    path('aplicaciones-facebook/', views.appsfb, name='appsfb'),
    path('contenido-redes-sociales/', views.smcontent, name='smcontent'),
    path('gestion-redes-sociales/', views.creationnetwork, name='creation-network'),
]
