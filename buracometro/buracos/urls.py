from django.contrib import admin
from django.urls import path, include
from .views import CadastroView, VerBuracosView
# from .views import InicioView, RankingView, VerNoMapaView

urlpatterns = [
    path('/cadastrar', CadastroView.as_view(), name='cadastrarView'),
    path('/ver-buracos', VerBuracosView.as_view(), name='verBuracosView'),
]