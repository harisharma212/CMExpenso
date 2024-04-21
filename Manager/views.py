from django.shortcuts import render
from django.views import View

# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, "about.html")


def do(request):
    return render(request, "do.html")


def portfolio(request):
    return render(request, "portfolio.html")


def contact(request):
    return render(request, "contact.html")