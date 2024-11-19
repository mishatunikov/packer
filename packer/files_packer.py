import zipfile

import pandas as pd
import py7zr

from packer.data_packer import create_csv, create_excel, create_txt
from timer import time_counter


class FilePacker:
    """
    Класс - упаковщик. Формирует файлы из объекта dict в различные форматы
    файлов (на данный момент доступно: csv, txt, xlsx). Создает из них архив
    zip ил 7z.
    """
    def __init__(self, data: dict) -> None:
        self.data = pd.DataFrame(data)

    @time_counter
    def create_zip(self):
        with zipfile.ZipFile('data.zip', 'w') as data_zip:
            data_zip.writestr('data.xlsx', create_excel(self.data).getvalue())
            data_zip.writestr('data.csv', create_csv(self.data).getvalue())
            data_zip.writestr('data.txt', create_txt(self.data).getvalue())

    @time_counter
    def create_7z(self):
        with py7zr.SevenZipFile('data.7z', 'w') as data_7z:
            data_7z.writestr(arcname='data.xlsx',
                             data=create_excel(self.data).getvalue())
            data_7z.writestr(arcname='data.csv',
                             data=create_csv(self.data).getvalue())
            data_7z.writestr(arcname='data.txt',
                             data=create_txt(self.data).getvalue())
