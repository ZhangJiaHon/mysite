from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'python/python.html')

def pyqt5_1(request):
    return render(request, 'python/pyqt5_1.html')

def pyqt5_2(request):
    return render(request, 'python/pyqt5_2.html')

def pyqt5_3(request):
    return render(request, 'python/pyqt5_3.html')