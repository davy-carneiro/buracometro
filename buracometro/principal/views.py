from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.db import IntegrityError

class InicioView(TemplateView):
    template_name = "principal/inicio.html"

class RankingView(TemplateView):
    template_name = "principal/ranking.html"