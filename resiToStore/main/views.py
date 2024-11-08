from django.shortcuts import render
from django.http import HttpResponse

def assembling(request):
    return render(request, 'main/assembling.html')

def popular(request):
    return render(request, 'main/popular.html')

def instruction(request):
    return render(request, 'main/instruction.html')