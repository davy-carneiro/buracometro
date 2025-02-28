from django.db import models

class Buraco(models.Model):
    titulo = models.CharField(max_length=255)  # Nome do objeto
    descricao = models.TextField()  # Descrição do objeto
    local = models.CharField(max_length=255)  # Local onde o objeto se encontra
    data_atual = models.DateTimeField(auto_now_add=True)  # Data e hora atuais (preenchido automaticamente)
    url_imagem = models.URLField()  # URL da imagem
    created_at = models.DateTimeField(auto_now_add=True)  # Data e hora de criação (preenchido automaticamente)
    updated_at = models.DateTimeField(auto_now=True)  # Data e hora de última atualização (atualizado automaticamente)

    def __str__(self):
        return self.nome