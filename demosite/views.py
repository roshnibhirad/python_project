from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')


def more(request):
    return render(request, 'more.html')


def contact(request):
    return render(request, 'contact.html')



