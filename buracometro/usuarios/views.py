from django.shortcuts import render
from django.views.generic import TemplateView

# class IndexView(TemplateView):
#     template_name = "usuarios/index.html"

class LoginView(TemplateView):
    template_name = "usuarios/login.html"

class RegisterView(TemplateView):
    template_name = "usuarios/register.html"