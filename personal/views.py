from django.shortcuts import render

from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    return render(request, 'personal/home.html')

def about(request):
    return render(request, 'personal/about.html')

def docker(request):
    return render(request, 'personal/docker.html')

def docker_2(request):
    return render(request, 'personal/docker_2.html')

def my_project(request):
    return render(request, 'personal/my_project.html')

