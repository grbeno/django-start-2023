from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# def home(request):
#     return HttpResponse("<h1>Hello, Django developer!</h1>")

class HomeView(TemplateView):
    template_name = 'home.html'


    
