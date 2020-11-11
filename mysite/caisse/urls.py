from django.urls import path
from . import views


urlpatterns = [
    path('caisse', views.caisse, name='caisse'),
    path('paiement', views.paiement, name='paiement'),
    path('retour', views.retour, name='retour'),
]
