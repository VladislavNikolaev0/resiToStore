from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
import json
from django.http import HttpResponse

def assembling(request):
    return render(request, 'main/assembling.html')

def popular(request):
    return render(request, 'main/popular.html')

def instruction(request):
    return render(request, 'main/instruction.html')

def processor_list(request):
    processors = Processor.objects.all()
    return render(request, 'main/processor_list.html', {'processors': processors})

def ram_list(request):
    rams = Ram.objects.all()
    return render(request, 'main/ram_list.html', {'rams': rams})

def motherbroad_list(request):
    motherbroads = MotherBroad.objects.all()
    return render(request,'main/motherbroad_list.html', {'motherbroads': motherbroads})

def powerUnit_list(request):
    powerUnits = PowerUnit.objects.all()
    return render(request,'main/powerUnit_list.html', {'powerUnits': powerUnits})