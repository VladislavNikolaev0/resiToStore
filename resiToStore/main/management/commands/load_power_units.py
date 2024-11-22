import pandas as pd
from django.core.management.base import BaseCommand
from main.models import PowerUnit

class Command(BaseCommand):
    help = "Load power unit data from Excel file"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Path to the Excel file")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            # Чтение данных из Excel
            data = pd.read_excel(file_path)

            # Добавление данных в базу
            for _, row in data.iterrows():
                PowerUnit.objects.create(
                    model=row['Model'],
                    power=row['Power'],
                    formFactor=row['Form factor'],
                    mainPowerConnector=row['Main power connector'],
                    connectorsForProcessor=row['Connectors for processor power supply'],
                    connectorsForVideoCard=row['Connectors for video card power supply'],
                    numbersForSata=row['Number of 15-pin SATA connectors'],
                    linePower12V=row['Line power 12 V'],
                    lineCurrent12V=row['Line current +12V'],
                    networkVoltage=row['Network input voltage range'],
                    country=row['Manufacturer Country'],
                    amount=row['Amount']
                )

            self.stdout.write(self.style.SUCCESS("Data successfully loaded into PowerUnit model!"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {e}"))