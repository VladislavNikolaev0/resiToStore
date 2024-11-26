import pandas as pd
from django.core.management.base import BaseCommand
from main.models import Hdd


class Command(BaseCommand):
    help = "Load HDD data from Excel file"

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
                    Hdd.objects.create(
                        model=row['Model'],  # Модель
                        hddCapacity=row['HDD Capacity'],  # Емкость жесткого диска
                        amountOfCacheMemory=row['amount of cache memory'],  # Объем кэш-памяти
                        spindleRotationSpeed=row['Spindle rotation speed'],  # Скорость вращения шпинделя
                        maximumDataTransferRate=row['Maximum data transfer rate'],  # Максимальная скорость передачи данных
                        interface=row['Interface'],  # Интерфейс
                        maximumOperatingTemperature=row['Maximum operating temperature'],  # Максимальная рабочая температура
                        countryOfOrigin=row['Country of origin'],  # Страна происхождения
                        amount=row['Amount']  # Цена
                    )
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Error on row {index + 1}: {row.to_dict()}"))
                    self.stderr.write(self.style.ERROR(f"Specific error: {e}"))

            self.stdout.write(self.style.SUCCESS("HDD data successfully loaded!"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {e}"))
