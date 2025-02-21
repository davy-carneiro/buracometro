from django.contrib import admin
from django.urls import path, include
from .views import InicioView, RankingView

urlpatterns = [
    path('', InicioView.as_view(), name='inicioView'),
    path('/inicio', InicioView.as_view(), name='inicioView'),
    path('/ranking', RankingView.as_view(), name='rankingView'),
]