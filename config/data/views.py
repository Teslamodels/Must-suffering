from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class One(TemplateView):
    template_name = 'index.html'

class Two(TemplateView):
    template_name = 'index2.html'

class Three(TemplateView):
    template_name = 'index3.html'

class Four(TemplateView):
    template_name = 'index4.html'