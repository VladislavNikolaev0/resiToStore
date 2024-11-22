import pandas as pd
from django.core.management.base import BaseCommand
from decimal import Decimal
from main.models import Processor


class Command(BaseCommand):
    help = "Load processor data from Excel file"

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
                    Processor.objects.create(
                        model=row['Model'],
                        socket=row['Socket'],
                        cores=row['Cores'],
                        releaseYear=row['Release Year'],
                        maxThreads=row['Max Threads'],
                        baseClock=Decimal(row['Base Clock (GHz)']),
                        turboClock=Decimal(row['Turbo Clock (GHz)']),
                        typeRam=row['RAM Type'],
                        maxRamSize=row['Max RAM Size (GB)'],
                        ramFrequency=row['RAM Frequency (MHz)'],
                        tdp=row['TDP (W)'],
                        maxTemp=row['Max Temp (°C)'],
                        country=row['Manufacturer Country'],
                        amount=row['Amount']
                    )
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Error on row {index + 1}: {row.to_dict()}"))
                    self.stderr.write(self.style.ERROR(f"Specific error: {e}"))

            self.stdout.write(self.style.SUCCESS("Processor data successfully loaded!"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {e}"))