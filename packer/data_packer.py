import io
from math import ceil

from pandas import DataFrame
from pyexcelerate import Workbook

from timer import time_counter


@time_counter
def create_excel(data: DataFrame) -> io.BytesIO:
    '''
    Создает файл .xlsx из DataFrame и возвращает буффер в, котором он создан.
    '''
    max_sheet_size = 1_048_576
    excel_buffer = io.BytesIO()
    workbook = Workbook()
    rows = [data.columns.to_list(), *data.values.tolist()]
    if len(rows) > max_sheet_size:
        for sheet_number, start, stop in [
                    (i + 1, max_sheet_size * i, max_sheet_size * (i + 1))
                    for i in range(ceil(len(rows) / max_sheet_size))
                ]:
            workbook.new_sheet(sheet_name=f'sheet_{sheet_number}',
                               data=rows[start:stop])
    else:
        workbook.new_sheet('sheet_1', data=rows)
    workbook.save(excel_buffer)
    excel_buffer.seek(0)
    return excel_buffer


@time_counter
def create_csv(data: DataFrame) -> io.BytesIO:
    '''
    Создает файл .csv из DataFrame и возвращает буффер в, котором он создан.
    '''
    csv_buffer = io.BytesIO()
    data.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)
    return csv_buffer


@time_counter
def create_txt(data: DataFrame) -> io.BytesIO:
    '''
    Создает файл .txt из DataFrame и возвращает буффер в, котором он создан.
    '''
    txt_buffer = io.BytesIO()
    data.to_csv(txt_buffer, sep=';', index=False)
    txt_buffer.seek(0)
    return txt_buffer
