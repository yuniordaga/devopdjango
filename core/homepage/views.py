from django.shortcuts import render
from django.view.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name='index.html'