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
    titulo = request.GET.get('titulo', '')
    descricao = request.GET.get('descricao', '')
    tamanho = request.GET.get('tamanho', '1')
    coordenadas = request.GET.get('coordenadas', '') 
    endereco = request.GET.get('endereco', '')

    variaveis = {
        'titulo': titulo,
        'descricao': descricao,
        'tamanho': tamanho,
        'coordenadas': coordenadas,
        'endereco': endereco,
    }

    return render(request, 'buracos/cadastro.html', variaveis)

# class CadastroSelecionarLocalView(TemplateView):
#     template_name = "buracos/cadastro-selecionar-local.html"

def cadastroSelecionarLocalView(request):
    titulo = ''
    descricao = ''
    tamanho = '1'

    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")
        tamanho = request.POST.get("tamanho")

    variaveis = {
        'titulo': titulo,
        'descricao': descricao,
        'tamanho': tamanho,
    }

    return render(request, "buracos/cadastro-selecionar-local.html", variaveis)

class VerBuracosView(TemplateView):
    template_name = "buracos/ver-buracos.html"

def passarLocalParaCadastroView(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")
        tamanho = request.POST.get("tamanho")
        coordenadas = request.POST.get("coordenadas")
        endereco = request.POST.get("endereco")

        parametros = {
            'titulo': titulo,
            'descricao': descricao,
            'tamanho': tamanho,
            'coordenadas': coordenadas,
            'endereco': endereco,
        }

        url = reverse('cadastrarView') + '?' + urlencode(parametros)  # Adiciona os parâmetros à URL

    return redirect(url)

def cadastroStore(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")
        coordenadas = request.POST.get("coordenadas")
        endereco = request.POST.get("endereco")
        tamanho = request.POST.get("tamanho")
        imagem = request.FILES["imagem"]

        caminho_pasta = os.path.join(settings.BASE_DIR, 'image')  # Pasta de destino
        nome_arquivo = imagem.name

        os.makedirs(caminho_pasta, exist_ok=True)

        caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)

        if os.path.exists(caminho_arquivo):
            base_nome, extensao = os.path.splitext(nome_arquivo)
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            nome_arquivo = f"{base_nome}_{timestamp}{extensao}"
            caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)

        # with open(caminho_arquivo, 'wb+') as destino:
        #     shutil.copyfileobj(imagem.file, destino)

        print(titulo)
        print(descricao)
        print(endereco)
        print(coordenadas)
        print(tamanho)
        print(imagem)
        print(caminho_arquivo.replace('\\', '/'))

    return redirect('cadastrarView')    