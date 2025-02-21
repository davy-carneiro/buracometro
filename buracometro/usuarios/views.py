from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.db import IntegrityError
from .models import CustomUser

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

def loginAction (request):
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")

        print(senha)

        try:
            userExists = CustomUser.objects.filter(username = usuario).exists()
            passIsValid = False
            
            if userExists:
                user = CustomUser.objects.filter(username = usuario).first()
                senhaComHash = user.password

                if user.password == senha:
                    passIsValid = True
                else:
                    passIsValid = check_password(senha, senhaComHash)
            
            if userExists and passIsValid:
                msg = "Login realizado com sucesso!"
                messages.success(request, msg)
                print(msg)

                return redirect('inicioView')
            else:
                msg = "Usuário e/ou senha inválido(s)"
                messages.error(request, msg)
                print(msg)

        except IntegrityError as e:
            msg = f"Erro: {e}"
            messages.error(request, msg)
            print(msg)
    
    return redirect('login')
