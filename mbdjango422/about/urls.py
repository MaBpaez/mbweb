from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    # Path NOSOTROS
    path('', views.us, name='us'),
]
