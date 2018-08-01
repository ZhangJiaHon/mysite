from django.shortcuts import render

from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    return render(request, 'personal/index.html')

def about(request):
    return render(request, 'personal/about.html')

def learn(request):
    return render(request, 'personal/learn.html')

def project(request):
    return render(request, 'personal/project.html')

