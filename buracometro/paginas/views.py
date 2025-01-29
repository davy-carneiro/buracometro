from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "paginas/index.html"


pip list

python -m venv venv

venv\Scripts\activate

pip install django

python manage.py startapp nome_app