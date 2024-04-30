from django.http import HttpResponse
from django.shortcuts import render

def test1(request):
    return HttpResponse("<h1>Test 1</h1>")

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about/index.html')