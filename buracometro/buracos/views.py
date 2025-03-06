from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import os
import shutil
from django.conf import settings
from django.urls import reverse
from urllib.parse import urlencode
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.db import IntegrityError
from datetime import datetime

# class CadastroView(TemplateView):
#     template_name = "buracos/cadastro.html"

def cadastroView(request):
    coordenadas = request.GET.get('coordenadas', '') 
    return render(request, 'buracos/cadastro.html', {'coordenadas': coordenadas})

class CadastroSelecionarLocalView(TemplateView):
    template_name = "buracos/cadastro-selecionar-local.html"

class VerBuracosView(TemplateView):
    template_name = "buracos/ver-buracos.html"

def passarLocalParaCadastroView(request):
    if request.method == "POST":
        coordenadas = request.POST.get("coordenadas")
        print(coordenadas)
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        # print(reverse('cadastroView'))
        parametros = {'coordenadas': coordenadas}  # Dicionário de parâmetros GET
        url = reverse('cadastrarView') + '?' + urlencode(parametros)  # Adiciona os parâmetros à URL

    return redirect(url)

def cadastroStore(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")
        coordenadas = request.POST.get("coordenadas")
        tamanho = request.POST.get("tamanho")
        imagem = request.FILES["imagem"]  # Obtém o arquivo enviado

        caminho_pasta = os.path.join(settings.BASE_DIR, 'image')  # Pasta de destino
        nome_arquivo = imagem.name

        os.makedirs(caminho_pasta, exist_ok=True)

        caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)

        if os.path.exists(caminho_arquivo):
            base_nome, extensao = os.path.splitext(nome_arquivo)
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            nome_arquivo = f"{base_nome}_{timestamp}{extensao}"
            caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)

        with open(caminho_arquivo, 'wb+') as destino:
            shutil.copyfileobj(imagem.file, destino)

        print(titulo)
        print(descricao)
        print(coordenadas)
        print(tamanho)
        print(caminho_arquivo.replace('\\', '/'))

    return redirect('cadastrarView')    