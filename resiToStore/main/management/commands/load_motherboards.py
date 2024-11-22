import pandas as pd
from django.core.management.base import BaseCommand
from main.models import MotherBroad


class Command(BaseCommand):
    help = "Load motherboard data from Excel file"

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
                    MotherBroad.objects.create(
                        model=row['Model'],
                        series=row['Series'],
                        fromFactor=row['Form Factor'],
                        height=row['Height'],
                        width=row['Width'],
                        socket=row['Socket'],
                        formFactorOfSupportedMemory=row['The form factor of supported memory'],
                        ramType=row['RAM Type'],
                        ramSlots=row['number of RAM slots'],
                        ramFrequency=row['RAM Frequency (MHz)'],
                        sataConnectors=row['Number of SATA Connectors'],
                        usbTypeASlots=row['Nuber of USB Type-A slots'],
                        country=row['Manufacturer Country'],
                        amount=row['Amount']
                    )
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Error on row {index + 1}: {row.to_dict()}"))
                    self.stderr.write(self.style.ERROR(f"Specific error: {e}"))

            self.stdout.write(self.style.SUCCESS("Motherboard data successfully loaded!"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {e}"))