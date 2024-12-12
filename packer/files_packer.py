import zipfile

import pandas as pd
import py7zr

from packer.data_packer import get_file
from utils import time_counter



class FilePacker:
    """
    Класс - упаковщик. Формирует файлы из объекта dict в различные форматы
    файлов (на данный момент доступно: csv, txt, xlsx). Создает из них архив
    zip ил 7z.
    """
    def __init__(self, data: dict, formats:tuple = ('csv', 'txt', 'xlsx',), filename: str = 'data') -> None:
        self.data = pd.DataFrame(data)
        self.formats = formats
        self.filename = filename

    @time_counter
    def create_zip(self):
        """Создает zip архив."""
        with zipfile.ZipFile('data.zip', 'w') as data_zip:
            for format_file in self.formats:
                data_zip.writestr(
                    zinfo_or_arcname='.'.join((self.filename, format_file)),
                    data=get_file(format_file, self.data)
                )

    @time_counter
    def create_7z(self):
        """Создает 7z архив."""
        with py7zr.SevenZipFile('data.7z', 'w') as data_7z:
            for format_file in self.formats:
                data_7z.writestr(
                    arcname='.'.join((self.filename, format_file)),
                    data=get_file(format_file, self.data)
                )

