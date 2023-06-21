# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    template = 'pages/about.html'
    return render(request, template)

def rules(request):
    template = 'pages/rules.html'
    return render(request, template)
