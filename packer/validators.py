import datetime
import re
from typing import Callable


def check_correct_date(input_date: str) -> bool:
    """
    Проверяет формат введенной даты.
    """
    try:
        datetime.datetime.strptime(input_date, '%d.%m.%Y')
        return True
    except Exception:
        return False


validators: dict[str, Callable] = {
    'ФИО': lambda fullname:
        re.fullmatch(r'[А-Яа-я]{2,25} [А-Яа-я]{2,25} [А-Яа-я]{2,25}',
                     fullname),
    'Дата рождения': check_correct_date,
    'Почтовый индекс': lambda index: re.fullmatch(r'[1-9][0-9]{5}',
                                                  index),
    'Город': lambda city: re.fullmatch(r'[А-Яа-я]{2,}', city),
    'Группа здоровья': lambda health_group: re.fullmatch(r'[123]',
                                                         health_group),
    'Профессия': lambda profession: re.fullmatch(r'[А-Яа-я]{2,}',
                                                 profession),

    'Место работы': lambda company: re.fullmatch(r'[А-Яа-я]{3,}',
                                                 company),
    'Имя пользователя': lambda username: re.fullmatch(r'@[A-z]{2,}',
                                                      username),
    'Электронная почта': lambda email: re.fullmatch(
        r'[A-Za-z]{2,}@[A-Za-z]{2,}\.[A-Za-z]{2,}', email),
    'Номер телефона': lambda phone_number: re.fullmatch(r'8[0-9]{10}',
                                                        phone_number),
    'archive_selection': lambda archive: re.fullmatch(r'[12]', archive),
    'validate_exit': lambda user_input: re.fullmatch(r'exit', user_input),
    'validate_format_selection': lambda user_input: re.fullmatch(r'[123]|(12|13|23|123)', user_input),
}

def validate_count_data(user_input: str) -> bool:
    """Проверяет корректность ввода количества генерируемых данных."""
    if not re.fullmatch(r'[1-9]\d*', user_input):
        return False
    return True