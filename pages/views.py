from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def inner(request):
    return render(request, 'pages/inner-page.html')

