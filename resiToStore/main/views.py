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
    sockets = set([processor.socket for processor in processors])
    cores = set([processor.cores for processor in processors])

    selectedCompany = request.POST.get("company", "")
    selectedSocket = request.POST.get("socket", "")
    selectedCore = request.POST.get("core", "")

    print(selectedCompany)

    if selectedCompany and selectedCompany != 'Производитель':
        processors = processors.filter(model__icontains=selectedCompany)

    if selectedSocket and selectedSocket != 'Сокет':
        processors = processors.filter(socket=selectedSocket)

    if selectedCore and selectedCore != 'Количество ядер':
        processors = processors.filter(cores=selectedCore)

    data = {
        'processors': processors,
        'sockets': sockets,
        'cores': cores,
    }

    return render(request, 'main/processor_list.html', data)

def ram_list(request):
    rams = Ram.objects.all()
    return render(request, 'main/ram_list.html', {'rams': rams})

def motherbroad_list(request):
    motherbroads = MotherBroad.objects.all()

    companies = set([board.model.split()[0] for board in motherbroads])
    formFactors = set([board.fromFactor for board in motherbroads])
    sockets = set([board.socket for board in motherbroads])

    selectedCompany = request.POST.get("company", "")
    selectedSocket = request.POST.get("socket", "")
    selectedFromFactor = request.POST.get("formFactor", "")

    if selectedCompany and selectedCompany != 'Производитель':
        motherbroads = motherbroads.filter(model__icontains=selectedCompany)

    if selectedSocket and selectedSocket != 'Сокет':
        motherbroads = motherbroads.filter(socket=selectedSocket)

    if selectedFromFactor and selectedFromFactor != 'Форм фактор':
        motherbroads = motherbroads.filter(fromFactor=selectedFromFactor)

    data = {
        'motherbroads': motherbroads,
        'companies': companies,
        'formFactors': formFactors,
        'sockets': sockets,
    }

    return render(request,'main/motherbroad_list.html', data)

def powerUnit_list(request):
    powerUnits = PowerUnit.objects.all()
    return render(request,'main/powerUnit_list.html', {'powerUnits': powerUnits})

def cooler_list(request):
    coolers = Cooler.objects.all()
    return render(request, 'main/cooler_list.html', {'coolers': coolers})

def corpus_list(request):
    corpuss = Corpus.objects.all()
    return render(request, 'main/corpus_list.html', {'corpuss': corpuss})

def videoCard_list(request):
    videoCards = VideoCard.objects.all()
    return render(request, 'main/videoCard_list.html', {'videoCards': videoCards})

def hdd_list(request):
    hdds = Hdd.objects.all()
    return render(request, 'main/hdd_list.html', {'hdds': hdds})

def ssd_list(request):
    ssds = Ssd.objects.all()
    return render(request, 'main/ssd_list.html', {'ssds': ssds})
