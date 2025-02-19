from django.contrib import admin
from django.urls import path, include
from .views import LoginView, RegisterView, registerStore

urlpatterns = [
    # path('', IndexView.as_view(), name='inicio'),
    path('login', LoginView.as_view(), name='login'),
    path('cadastro', RegisterView.as_view(), name='register'),
    path('cadastro/cadastrar', registerStore, name='registerStore'),
]