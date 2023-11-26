from django.shortcuts import render
from django.views.generic import ListView
from .models import Post3
# Create your views here.

class Seven(ListView):
    model = Post3
    template_name = 'index7.html'