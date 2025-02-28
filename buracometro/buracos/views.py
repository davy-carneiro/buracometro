from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.db import IntegrityError

class CadastroView(TemplateView):
    template_name = "buracos/cadastro.html"

class VerBuracosView(TemplateView):
    template_name = "buracos/ver-buracos.html"