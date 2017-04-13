from django.shortcuts import render

from django.views.generic import TemplateView, DetailView, ListView, CreateView

from .models import Response

class HomeView(TemplateView):
    template_name='home.html'
    
    
class ResponseCreateView(CreateView):
    model = Response
    template_name='respond.html'
    fields = ['title','message','thread','parent_response']

