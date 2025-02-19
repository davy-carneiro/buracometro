from django.contrib import admin
from django.urls import path, include
from .views import LoginView, RegisterView, registerStore, loginAction

urlpatterns = [
    # path('', IndexView.as_view(), name='inicio'),
    path('login', LoginView.as_view(), name='login'),
    path('login/logar', loginAction, name='loginAction'),
    path('cadastro', RegisterView.as_view(), name='register'),
    path('cadastro/cadastrar', registerStore, name='registerStore'),
]