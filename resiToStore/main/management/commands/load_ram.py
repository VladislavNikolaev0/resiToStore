import pandas as pd
from django.core.management.base import BaseCommand
from main.models import Ram


class Command(BaseCommand):
    help = "Load RAM data from Excel file"

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
                    Ram.objects.create(
                        model=row['Model'],
                        type=row['Memory type'],
                        capacity=row['Memory capacity'],
                        clockSpeed=row['Clock Speed'],
                        formFactor=row['Form factor'],
                        rgbBacklight=row['Rgb backlight'],
                        country=row['Manufacturer Country'],
                        amount=row['Amount']
                    )
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Error on row {index + 1}: {row.to_dict()}"))
                    self.stderr.write(self.style.ERROR(f"Specific error: {e}"))

            self.stdout.write(self.style.SUCCESS("RAM data successfully loaded!"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {e}"))