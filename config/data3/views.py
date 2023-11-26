from django.shortcuts import render
from django.views.generic import ListView
from .models import Post2
# Create your views here.


class Six(ListView):
    model = Post2
    template_name = 'index6.html'