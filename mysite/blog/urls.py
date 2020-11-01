from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('provider', views.provider, name='provider'),
    path('article', views.article, name='article'),
]
