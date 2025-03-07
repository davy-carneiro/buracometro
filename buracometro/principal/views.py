from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.db import IntegrityError
from buracos.models import Buraco


class InicioView(TemplateView):
    template_name = "principal/inicio.html"

#class RankingView(TemplateView):
  #  template_name = "principal/ranking.html"

def rankingView(request):
    buracos = Buraco.objects.order_by('-tamanho')
    variaveis = {
        'buracos':buracos,
    }
    return render(request, 'principal/ranking.html', variaveis)

class VerNoMapaView(TemplateView):
    template_name = "principal/ver-no-mapa.html"