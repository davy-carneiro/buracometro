from django.contrib import admin
from django.urls import path, include
from .views import CadastroView, VerBuracosView, cadastroStore
# from .views import InicioView, RankingView, VerNoMapaView

urlpatterns = [
    path('/cadastrar', CadastroView.as_view(), name='cadastrarView'),
    path('/cadastrar/salvar', cadastroStore, name='cadastroStore'),
    path('/ver-buracos', VerBuracosView.as_view(), name='verBuracosView'),
]