from django.contrib import admin
from .models import CustomUser

# Abra o arquivo admin.py do seu app e adicione:

admin.site.register(CustomUser)

