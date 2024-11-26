import pandas as pd
from django.core.management.base import BaseCommand
from main.models import Corpus


class Command(BaseCommand):
    help = "Load corpus data from Excel file"

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
                    Corpus.objects.create(
                        model=row['Model'],  # Модель
                        orientationOfTheMotherboard=row['Orientation of the motherboard'],  # Ориентация материнской платы
                        width=row['Width'],  # Ширина
                        height=row['Height'],  # Высота
                        weight=row['Weight'],  # Вес
                        mainColor=row['Main color'],  # Основной цвет
                        additionalColor=row['Additional color'],  # Доп. цвета
                        housingMaterial=row['Housing material'],  # Материал корпуса
                        formFactorOfCompatibleBoards=row['Form factor of compatible boards'],  # Форм-фактор совместимой платы
                        theFormFactorOfCompatiblePowerSupplies=row['The form factor of compatible power supplies'],  # Форм-фактор совместимого БП
                        countryOfOrigin=row['Country of origin'],  # Страна происхождения
                        amount=row['Amount']  # Цена
                    )
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Error on row {index + 1}: {row.to_dict()}"))
                    self.stderr.write(self.style.ERROR(f"Specific error: {e}"))

            self.stdout.write(self.style.SUCCESS("Corpus data successfully loaded!"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {e}"))
