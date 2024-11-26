import pandas as pd
from django.core.management.base import BaseCommand
from main.models import VideoCard


class Command(BaseCommand):
    help = "Load video card data from Excel file"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Path to the Excel file")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            # Чтение данных из Excel
            data = pd.read_excel(file_path)

            # Добавление данных в базу
            for index, row in data.iterrows():
                try:
                    VideoCard.objects.create(
                        model=row['Model'],  # Модель
                        Microarchitecture=row['Microarchitecture'],  # Микроархитектура
                        theStandardFrequencyOfOperationOfTheVideoChip=row['The standard frequency of operation of the video chip'],  # Стандартная частота работы видеочипа
                        turboFrequency=row['Turbo frequency'],  # Турбочастота
                        amountOfVideoMemory=row['amount of video memory'],  # Количество видеопамяти
                        memoryType=row['Memory type'],  # Тип памяти
                        theBitDepthOfTheMemoryBus=row['The bit depth of the memory bus'],  # Разрядность шины памяти
                        theNumberOfMonitorsConnectedAtTheSameTime=row['The number of monitors connected at the same time'],  # Количество мониторов
                        countryOfOrigin=row['Country of origin'],  # Страна происхождения
                        amount=row['Amount']  # Цена
                    )
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Error on row {index + 1}: {row.to_dict()}"))
                    self.stderr.write(self.style.ERROR(f"Specific error: {e}"))

            self.stdout.write(self.style.SUCCESS("Video card data successfully loaded!"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {e}"))
