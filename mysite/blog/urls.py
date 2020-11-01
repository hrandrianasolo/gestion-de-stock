from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('provider', views.provider, name='provider'),
    path('edit_provider/<provide_id>', views.edit_provider, name='edit_provider'),
    path('new_provider', views.new_provider, name='new_provider'),
    path('delete_provider/<provide_id>', views.delete_provider, name='delete_provider'),
    path('article', views.article, name='article'),
    path('edit_article/<article_id>', views.edit_article, name='edit_article'),
    path('article_bt', views.article_below_threshold, name='article_below_threshold'),
    path('new_article', views.new_article, name='new_article'),
    path('delete_article/<article_id>', views.delete_article, name='delete_article'),
]
