from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Path NOSOTROS
    path('', views.post_list, name='post-list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('categorias/<int:category_id>/<slug:category_name>/', views.post_list,
         name='category'),

    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail,
         name='post-detail'),
    path('<int:post_id>/compartir-por-email/', views.post_share, name='post_share'),
    path('<slug:commented_post>/comentario-enviado/', views.comment_successfully,
         name='comment_sent'),
    # path('categorias/<int:category_id>/', views.get_category, name='category'),
    path('search/', views.post_search, name='post_search'),
]
