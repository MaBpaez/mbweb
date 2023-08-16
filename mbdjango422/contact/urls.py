from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    # Path CONTACTO
    path('', views.contact, name='contacto'),
]
