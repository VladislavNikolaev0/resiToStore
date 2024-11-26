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

    companies = set([ram.model.split()[0] for ram in rams])
    type = set([ram.type for ram in rams])
    capacity = set([ram.capacity for ram in rams])

    selectedCompany = request.POST.get("company", "")
    selectedType = request.POST.get("type", "")
    selectedCapacity = request.POST.get("capacity", "")

    if selectedCompany and selectedCompany != 'Производитель':
        rams = rams.filter(model__icontains=selectedCompany)

    if selectedType and selectedType != 'Тип ОЗУ':
        rams = rams.filter(type=selectedType)

    if selectedCapacity and selectedCapacity != 'Емкость':
        rams = rams.filter(capacity=selectedCapacity)

    data = {
        'rams': rams,
        'companies': companies,
        'type': type,
        'capacity': capacity,
    }

    return render(request, 'main/ram_list.html', data)

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

    companies = set([unit.model.split()[0] for unit in powerUnits])

    companies.remove('be')
    companies.remove('Cooler')
    companies.add('be quiet!')
    companies.add('Cooler Master')
    powers = set([unit.power for unit in powerUnits])
    formFactors = set([unit.formFactor for unit in powerUnits])

    selectedCompany = request.POST.get("company", "")
    selectedPower = request.POST.get("power", "")
    selectedformFactor = request.POST.get("formFactor", "")

    if selectedCompany and selectedCompany != 'Производитель':
        powerUnits = powerUnits.filter(model__icontains=selectedCompany)

    if selectedPower and selectedPower != 'Мощность':
        powerUnits = powerUnits.filter(power=selectedPower)

    if selectedformFactor and selectedformFactor != 'Форм фактор':
        powerUnits = powerUnits.filter(formFactor=selectedformFactor)

    data = {
        'powerUnits': powerUnits,
        'companies': companies,
        'powers': powers,
        'formFactors': formFactors,
    }

    return render(request,'main/powerUnit_list.html', data)

def cooler_list(request):
    coolers = Cooler.objects.all()

    companies = set([item.model.split()[0] for item in coolers])

    companies.remove('be')
    companies.remove('Cooler')
    companies.add('be quiet!')
    companies.add('Cooler Master')
    powers = set([unit.powerDissipation for unit in coolers])
    types = set([unit.type for unit in coolers])

    selectedCompany = request.POST.get("company", "")
    selectedPower = request.POST.get("power", "")
    selectedType = request.POST.get("type", "")

    if selectedCompany and selectedCompany != 'Производитель':
        coolers = coolers.filter(model__icontains=selectedCompany)

    if selectedPower and selectedPower != 'Рассеиваемая мощность':
        coolers = coolers.filter(powerDissipation=selectedPower)

    if selectedType and selectedType != 'Тип':
        coolers = coolers.filter(type=selectedType)

    data = {
        'coolers': coolers,
        'companies': companies,
        'powers': powers,
        'types': types,
    }

    return render(request, 'main/cooler_list.html', data)

def corpus_list(request):
    corpuss = Corpus.objects.all()

    companies = set([item.model.split()[0] for item in corpuss])

    companies.remove('Cooler')
    companies.add('Cooler Master')
    # formFactorsOfCompatibleBoards = [unit.formFactorOfCompatibleBoards for unit in corpuss]
    colors = set([unit.mainColor for unit in corpuss])

    selectedCompany = request.POST.get("company", "")
    selectedBoardFormFactor = request.POST.get("boardFormFactor", "")
    selectedColor = request.POST.get("color", "")

    if selectedCompany and selectedCompany != 'Производитель':
        corpuss = corpuss.filter(model__icontains=selectedCompany)

    if selectedBoardFormFactor and selectedBoardFormFactor != 'Форм фактор совместимой платы':
        corpuss = corpuss.filter(formFactorOfCompatibleBoards__icontains=selectedBoardFormFactor)

    if selectedColor and selectedColor != 'Основной цвет':
        corpuss = corpuss.filter(mainColor=selectedColor)

    data = {
        'corpuss': corpuss,
        'companies': companies,
        # 'boardFormFactors': formFactorsOfCompatibleBoards,
        'colors': colors,
    }

    return render(request, 'main/corpus_list.html', data)

def videoCard_list(request):
    videoCards = VideoCard.objects.all()

    companies = set([card.model.split()[0] for card in videoCards])
    Microarchitectures = set([card.Microarchitecture for card in videoCards])
    amountOfVideoMemorys = set([card.amountOfVideoMemory for card in videoCards])

    selectedCompany = request.POST.get("company", "")
    selectedSockeMicroarchitecture = request.POST.get("Microarchitecture", "")
    selectedamountOfVideoMemory = request.POST.get("amountOfVideoMemory", "")

    if selectedCompany and selectedCompany != 'Производитель':
        videoCards = videoCards.filter(model__icontains=selectedCompany)

    if selectedSockeMicroarchitecture and selectedSockeMicroarchitecture != 'Микроархитектура':
        videoCards = videoCards.filter(Microarchitecture=selectedSockeMicroarchitecture)

    if selectedamountOfVideoMemory and selectedamountOfVideoMemory != 'Количество видео памяти':
        videoCards = videoCards.filter(amountOfVideoMemory=selectedamountOfVideoMemory)

    data = {
        'videoCards': videoCards,
        'companies': companies,
        'Microarchitectures': Microarchitectures,
        'amountOfVideoMemorys': amountOfVideoMemorys,
    }

    return render(request, 'main/videoCard_list.html', data)

def hdd_list(request):
    hdds = Hdd.objects.all()

    companies = set([hdd.model.split()[0] for hdd in hdds])
    hddCapacitys = set([hdd.hddCapacity for hdd in hdds])
    amountOfCacheMemorys = set([hdd.amountOfCacheMemory for hdd in hdds])

    selectedCompany = request.POST.get("company", "")
    selectedhddCapacity = request.POST.get("hddCapacity", "")
    selectedamountOfCacheMemory = request.POST.get("amountOfCacheMemory", "")

    if selectedCompany and selectedCompany != 'Производитель':
        hdds = hdds.filter(model__icontains=selectedCompany)

    if selectedhddCapacity and selectedhddCapacity != 'Емкость':
        hdds = hdds.filter(hddCapacity=selectedhddCapacity)

    if selectedamountOfCacheMemory and selectedamountOfCacheMemory != 'Количество кеш памяти':
        hdds = hdds.filter(amountOfCacheMemory=selectedamountOfCacheMemory)

    data = {
        'hdds': hdds,
        'companies': companies,
        'hddCapacitys': hddCapacitys,
        'amountOfCacheMemorys': amountOfCacheMemorys,
    }

    return render(request, 'main/hdd_list.html', data)

def ssd_list(request):
    ssds = Ssd.objects.all()

    companies = set([ssd.model.split()[0] for ssd in ssds])
    storageCapacitys = set([ssd.storageCapacity for ssd in ssds])
    controllers = set([ssd.controller for ssd in ssds])

    selectedCompany = request.POST.get("company", "")
    selectedstorageCapacity = request.POST.get("storageCapacity", "")
    selectedcontroller = request.POST.get("controller", "")

    if selectedCompany and selectedCompany != 'Производитель':
        ssds = ssds.filter(model__icontains=selectedCompany)

    if selectedstorageCapacity and selectedstorageCapacity != 'Емкость':
        ssds = ssds.filter(storageCapacity=selectedstorageCapacity)

    if selectedcontroller and selectedcontroller != 'Контроллер':
        ssds = ssds.filter(controller=selectedcontroller)

    data = {
        'ssds': ssds,
        'companies': companies,
        'storageCapacitys': storageCapacitys,
        'controllers': controllers,
    }

    return render(request, 'main/ssd_list.html', data)
