from django.urls import path
from . import views

app_name = 'graphicdesign'

urlpatterns = [
    # Path DISEÑO GRÁFICO
    path('diseno-imagen-corporativa/', views.corporateimage, name='corporate-image'),
    path('diseno-logotipo/', views.logotipo, name='logotipo'),
]
