import pandas as pd
from django.core.management.base import BaseCommand
from main.models import Cooler


class Command(BaseCommand):
    help = "Load cooler data from Excel file"

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
                    Cooler.objects.create(
                        type=row['Type'],  # Тип
                        model=row['Model'],  # Модель
                        powerDissipation=row['Power dissipation'],  # Рассеиваемая мощность
                        typeOfConstruction=row['Type of construction'],  # Тип конструкции
                        baseMaterial=row['Base material'],  # Основной металл
                        radiatorMaterial=row['Radiator Material'],  # Металл радиатора
                        minimumRotationSpeed=row['Minimum rotation speed'],  # Мин. скорость вращения
                        maximumStaticPressure=row['Maximum static pressure'],  # Макс. статическое давление
                        connectorForConnectingFans=row['Connector for connecting fans'],  # Разъем подключения вентиляторов
                        maximumRotationSpeed=row['Maximum rotation speed'],  # Макс. скорость вращения
                        ratedCurrent=row['Rated current'],  # Номинальный ток
                        ratedVoltage=row['Rated voltage'],  # Номинальное напряжение
                        countryOfOrigin=row['Country of origin'],  # Страна происхождения
                        amount=row['Amount']  # Цена
                    )
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Error on row {index + 1}: {row.to_dict()}"))
                    self.stderr.write(self.style.ERROR(f"Specific error: {e}"))

            self.stdout.write(self.style.SUCCESS("Cooler data successfully loaded!"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {e}"))
