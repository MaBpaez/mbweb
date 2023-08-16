from django.urls import path
from . import views

app_name = 'webdesign'

urlpatterns = [
    # Path DISEÑO WEB
    path('desarrollo-web-a-medida/', views.webmedida, name='custom-web'),
    path('dominio-web/', views.hosting, name='hosting'),
    path('landing-page/', views.landingpage, name='landing'),
    path('blog-a-medida/', views.customblog, name='custom-blog'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('mantenimiento-web/', views.webmaintenance, name='web-maintenance'),
]
