from django.db import models
from tkinter.constants import CASCADE

# Create your models here.

class Processor(models.Model):
    model = models.CharField(max_length=255, verbose_name="Модель")
    socket = models.CharField(max_length=255, verbose_name="Сокет")
    cores = models.IntegerField(verbose_name="Количество ядер")
    releaseYear = models.IntegerField(verbose_name="Год релиза")
    maxThreads = models.IntegerField(verbose_name="Максимальное количество потоков")
    baseClock = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Базовая частота")
    turboClock = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Частота в турбо режиме")
    typeRam = models.CharField(max_length=255, verbose_name="Тип поддерживаемой озу")
    maxRamSize = models.IntegerField(verbose_name="Максимальное поличество озу (Гб)")
    ramFrequency = models.IntegerField(verbose_name="Частота оперативной памяти (МГц)")
    tdp = models.IntegerField(verbose_name="Тепловыделение (Вт)")
    maxTemp = models.IntegerField(verbose_name="Максимальная температура (°C)")
    country = models.CharField(max_length=255, verbose_name="Страна производителя")
    amount = models.IntegerField(verbose_name="Цена ($)")

    def __str__(self):
        return f"{self.model}"

    class Meta:
        verbose_name = 'Процессор'
        verbose_name_plural = 'Процессоры'

class MotherBroad(models.Model):
    model = models.CharField(max_length=255, verbose_name="Модель")
    series = models.CharField(max_length=255, verbose_name="Серия")
    fromFactor = models.CharField(max_length=255, verbose_name="Форм фактор")
    height = models.IntegerField(verbose_name="Высота (мм)")
    width = models.IntegerField(verbose_name="Ширана (мм)")
    socket = models.CharField(max_length=255, verbose_name="Сокет")
    formFactorOfSupportedMemory = models.CharField(max_length=255, verbose_name="Форм фактор озу")
    ramType = models.CharField(max_length=255, verbose_name="Тип озу")
    ramSlots = models.IntegerField(verbose_name="Количество слотов озу")
    ramFrequency = models.IntegerField(verbose_name="Частота оперативной памяти (МГц)")
    sataConnectors = models.IntegerField(verbose_name="Количество портов Сата")
    usbTypeASlots = models.IntegerField(verbose_name="Количество потров usb type-A")
    country = models.CharField(max_length=255, verbose_name="Страна производителя")
    amount = models.IntegerField(verbose_name="Цена ($)")

    def __str__(self):
        return f"{self.model}"

    class Meta:
        verbose_name = 'Материнская плата'
        verbose_name_plural = 'Материнскаие платы'


class Ram(models.Model):
    model = models.CharField(max_length=255, verbose_name="Модель")
    type = models.CharField(max_length=255, verbose_name="Тип озу")
    capacity = models.CharField(max_length=255, verbose_name="Емкость")
    clockSpeed = models.IntegerField(verbose_name="Частота")
    formFactor = models.CharField(max_length=255, verbose_name="Форм фактор")
    rgbBacklight = models.CharField(max_length=255, verbose_name="RGB подцветка")
    country = models.CharField(max_length=255, verbose_name="Страна производителя")
    amount = models.IntegerField(verbose_name="Цена ($)")

    def __str__(self):
        return f"{self.model}"

    class Meta:
        verbose_name = 'Оперативная память'
        verbose_name_plural = 'Оперативная память'

class PowerUnit(models.Model):
    model = models.CharField(max_length=255, verbose_name="Модель")
    power = models.IntegerField(verbose_name="Мощность")
    formFactor = models.CharField(max_length=255, verbose_name="Форм фактор")
    mainPowerConnector = models.CharField(max_length=255, verbose_name="Основной разъем питания")
    connectorsForProcessor = models.CharField(max_length=255, verbose_name="Разъемы для питания процессора")
    connectorsForVideoCard = models.CharField(max_length=255, verbose_name="Разъемы для питания видеокарты")
    numbersForSata = models.IntegerField(verbose_name="Количество разъемов 15-pin SATA")
    linePower12V = models.IntegerField(verbose_name="Мощность по линии 12 В")
    lineCurrent12V = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Ток по линии +12 В")
    networkVoltage = models.CharField(max_length=255, verbose_name="Диапазон входного напряжения сети")
    country = models.CharField(max_length=255, verbose_name="Страна производителя")
    amount = models.IntegerField(verbose_name="Цена ($)")

    def __str__(self):
        return f"{self.model}"

    class Meta:
        verbose_name = 'Блок питания'
        verbose_name_plural = 'Блоки питания'

class Cooler(models.Model):
    type = models.CharField(max_length=255, verbose_name="Тип")
    model = models.CharField(max_length=255, verbose_name="Модель")
    powerDissipation = models.IntegerField(verbose_name="Рассеиваемая мощность")
    typeOfConstruction = models.CharField(max_length=255, verbose_name="Тип Конструкции")
    baseMaterial = models.CharField(max_length=255, verbose_name="Основной металл")
    radiatorMaterial = models.CharField(max_length=255, verbose_name="Металл радиатора")
    minimumRotationSpeed = models.IntegerField(verbose_name="Минимальная скорость вращения")
    maximumStaticPressure = models.CharField(max_length=255, verbose_name="Максимальное статическое давление")
    connectorForConnectingFans = models.CharField(max_length=255, verbose_name="Разъем для Подключения Вентиляторов")
    maximumRotationSpeed = models.IntegerField(verbose_name="Максимальная скорость вращения")
    ratedCurrent = models.CharField(max_length=255, verbose_name="Номинальный ток")
    ratedVoltage = models.IntegerField(verbose_name="Номинальное напряжение")
    countryOfOrigin = models.CharField(max_length=255, verbose_name="Страна происхождения")
    amount = models.IntegerField(verbose_name="Цена")

    def __str__(self):
        return f"{self.model}"

    class Meta:
        verbose_name = 'Система охлаждения'
        verbose_name_plural = 'Системы охлаждения'

class Corpus(models.Model):
    model = models.CharField(max_length=255, verbose_name="Модель")
    orientationOfTheMotherboard = models.CharField(max_length=255, verbose_name="Ориентация материнской платы")
    width = models.IntegerField(verbose_name="Ширина")
    height = models.IntegerField(verbose_name="Высота")
    weight = models.IntegerField(verbose_name="Вес")
    mainColor = models.CharField(max_length=255, verbose_name="Основной цвет")
    additionalColor = models.CharField(max_length=255, verbose_name="Доп. цвета")
    housingMaterial = models.CharField(max_length=255, verbose_name="Материал корпуса")
    formFactorOfCompatibleBoards = models.CharField(max_length=255, verbose_name="Форм фактор совместимой платы")
    theFormFactorOfCompatiblePowerSupplies = models.CharField(max_length=255, verbose_name="Форм фатор совместимого блока питания")
    countryOfOrigin = models.CharField(max_length=255, verbose_name="Страна происхождения")
    amount = models.IntegerField(verbose_name="Цена")

    def __str__(self):
        return f"{self.model}"

    class Meta:
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпусы'

class VideoCard(models.Model):
    model = models.CharField(max_length=255, verbose_name="Модель")
    Microarchitecture = models.CharField(max_length=255, verbose_name="Микроархитектура")
    theStandardFrequencyOfOperationOfTheVideoChip = models.IntegerField(verbose_name="Стандартная Частота Работы Видеочипа")
    turboFrequency = models.IntegerField(verbose_name="частота турбонаддува")
    amountOfVideoMemory = models.IntegerField(verbose_name="Количество видео памяти")
    memoryType = models.CharField(max_length=255, verbose_name="Тип памяти")
    theBitDepthOfTheMemoryBus = models.IntegerField(verbose_name="Разрядность Шины Памяти")
    theNumberOfMonitorsConnectedAtTheSameTime = models.IntegerField(verbose_name="Количество мониторов подключаемых одновремменно")
    countryOfOrigin = models.CharField(max_length=255, verbose_name="Страна происхождения")
    amount = models.IntegerField(verbose_name="Цена")

    def __str__(self):
        return f"{self.model}"

    class Meta:
        verbose_name = 'Видео карта'
        verbose_name_plural = 'Видео карты'

class Hdd(models.Model):
    model = models.CharField(max_length=255, verbose_name="Модель")
    hddCapacity = models.IntegerField(verbose_name="Емкость жесткого диска")
    amountOfCacheMemory = models.IntegerField(verbose_name="Объем Кэш-памяти")
    spindleRotationSpeed = models.IntegerField(verbose_name="скорость вращения шпинделя")
    maximumDataTransferRate = models.IntegerField(verbose_name="максимальная скорость передачи данных")
    interface = models.CharField(max_length=255, verbose_name="Интерфейс")
    maximumOperatingTemperature = models.CharField(max_length=255, verbose_name="максимальная рабочая температура")
    countryOfOrigin = models.CharField(max_length=255, verbose_name="Страна происхождения")
    amount = models.IntegerField(verbose_name="Цена")

    def __str__(self):
        return f"{self.model}"

    class Meta:
        verbose_name = 'HDD'
        verbose_name_plural = 'HDDs'

class Ssd(models.Model):
    model = models.CharField(max_length=255, verbose_name="Модель")
    storageCapacity = models.IntegerField(verbose_name="емкость запоминающего устройства")
    connectionConnector = models.CharField(max_length=255, verbose_name="соединительный разъем")
    controller = models.CharField(max_length=255, verbose_name="контроллер")
    maximumSequentialReadSpeed = models.IntegerField(verbose_name="максимальная скорость последовательного чтения")
    maximumSequentialRecordingSpeed = models.IntegerField(verbose_name="максимальная скорость последовательной записи")
    countryOfOrigin = models.CharField(max_length=255, verbose_name="Страна происхождения")
    amount = models.IntegerField(verbose_name="Цена")

    def __str__(self):
        return f"{self.model}"

    class Meta:
        verbose_name = 'SSD'
        verbose_name_plural = 'SSDs'