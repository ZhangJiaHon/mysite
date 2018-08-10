from django.shortcuts import render

from django.http import HttpResponse


def learn(request):
    return render(request, 'learn/learn.html')

def html(request):
    return render(request, 'learn/html.html')

def css(request):
    return render(request, 'learn/css.html')

def javascript(request):
    return render(request, 'learn/javascript.html')

def docker(request):
    return render(request, 'learn/docker.html')

def foundation(request):
    return render(request, 'learn/foundation.html')

def laravel(request):
    return render(request, 'learn/laravel.html')
