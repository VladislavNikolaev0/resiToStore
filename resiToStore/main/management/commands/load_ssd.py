import pandas as pd
from django.core.management.base import BaseCommand
from main.models import Ssd


class Command(BaseCommand):
    help = "Load SSD data from Excel file"

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
                    Ssd.objects.create(
                        model=row['Model'],  # Модель
                        storageCapacity=row['Storage capacity'],  # Емкость запоминающего устройства
                        connectionConnector=row['Connection connector'],  # Соединительный разъем
                        controller=row['controller'],  # Контроллер
                        maximumSequentialReadSpeed=row['Maximum sequential read speed'],  # Макс. скорость чтения
                        maximumSequentialRecordingSpeed=row['Maximum sequential recording speed'],  # Макс. скорость записи
                        countryOfOrigin=row['Country of origin'],  # Страна происхождения
                        amount=row['Amount']  # Цена
                    )
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Error on row {index + 1}: {row.to_dict()}"))
                    self.stderr.write(self.style.ERROR(f"Specific error: {e}"))

            self.stdout.write(self.style.SUCCESS("SSD data successfully loaded!"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {e}"))
