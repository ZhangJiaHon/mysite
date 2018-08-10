from django.shortcuts import render

from django.http import HttpResponse


def project(request):
    return render(request, 'project/project.html')

def shopcart(request):
    return render(request, 'project/project_shopcart.html')

def flaskscrapy(request):
    return render(request, 'project/project_flaskscrapy.html')

