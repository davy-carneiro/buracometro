from django.contrib import admin
from django.urls import path, include
from .views import *
# from .views import InicioView, RankingView, VerNoMapaView

urlpatterns = [
    path('/cadastrar', cadastroView, name='cadastrarView'),
    path('/cadastrar/selecionar-local', CadastroSelecionarLocalView.as_view(), name='cadastroSelecionarLocalView'),
    path('/cadastrar/selecionar-local/selecionando', passarLocalParaCadastroView, name='passarLocalParaCadastroView'),
    path('/cadastrar/salvar', cadastroStore, name='cadastroStore'),
    path('/ver-buracos', VerBuracosView.as_view(), name='verBuracosView'),
]