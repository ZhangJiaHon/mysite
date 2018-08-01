from django.shortcuts import render

from django.http import HttpResponse


def python(request):
    return render(request, 'python/python.html')

def pyqt51(request):
    return render(request, 'python/pyqt51.html')

def pyqt52(request):
    return render(request, 'python/pyqt52.html')

def pyqt53(request):
    return render(request, 'python/pyqt53.html')