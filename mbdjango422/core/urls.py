from django.urls import path
from . import views

urlpatterns = [
    # Path del core
    path('', views.home, name='home'),
    path('formulario-enviado/', views.form_successfully, name='form_success'),
    path('save-token/', views.save_token, name='save_token'),
]
