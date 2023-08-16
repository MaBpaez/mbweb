from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    # Path PORTFOLIO
    path("", views.portafolio, name="portafolio"),
    path(
        'categorias/<int:category_id>/<slug:category_name>/',
        views.portafolio,
        name='portfolio_category',
    ),
    # path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.work_detail,
    #      name='work-detail'),
]
