from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import CustomUser
from django.contrib import messages
from django.db import IntegrityError


# class IndexView(TemplateView):
#     template_name = "usuarios/index.html"

class LoginView(TemplateView):
    template_name = "usuarios/login.html"

class RegisterView(TemplateView):
    template_name = "usuarios/register.html"

def registerStore(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")
        dataNascimento = request.POST.get("data-nascimento")

        try:
            user = CustomUser.objects.create(
                name=nome, 
                username=usuario, 
                password=senha, 
                date_of_birth=dataNascimento
            )
            user.save()

            msg = "Usuário criado com sucesso!"
            messages.success(request, msg)
        except IntegrityError as e:
            msg = f"Erro ao criar usuário: {e}"
            messages.error(request, msg)

        return redirect('register')
        # return render(request, "sucesso")

    return redirect("register") # get