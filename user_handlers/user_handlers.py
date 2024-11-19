import datetime
import logging
import re
from collections import defaultdict, deque
from typing import Callable

from data_generator import DataGenerator
from lexicon import CELLS_NAME, LEXICON


def check_correct_date(input_date: str) -> bool:
    '''
    Проверяет формат введенной даты.
    '''
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
}


def greetings() -> int:
    '''
    Выводит стартовое сообщение для пользователя и
    запрашивает выбор ввода от него.
    '''
    print(LEXICON['greetings'])
    while True:
        user_input = input()
        if validators['validate_exit'](user_input):
            return 0
        try:
            result = int(user_input)
            if 1 <= result <= 3:
                return result
            else:
                raise ValueError
        except Exception:
            print('Введите от 1 до 3')
            continue


def validate_count_data(user_input: str) -> bool:
    '''Проверяет корректность ввода количества генерируемых данных.'''
    if not re.fullmatch(r'[1-9]\d*', user_input):
        return False
    return True


def user_manual_entry() -> defaultdict[str, deque]:
    '''
    Обрабатывает ручной ввод от пользователя.
    Возвращает словарь, состоящий из введенных данных.
    '''
    logging.info('Пользователь выбрал ручной ввод.')
    data: defaultdict[str, deque] = defaultdict(deque)

    while True:
        try:
            user_input = input(LEXICON['data_count_manual'])
            if validators['validate_exit'](user_input):
                logging.info('Пользователь прервал ввод данных.')
                return data

            if not validate_count_data(user_input):
                raise ValueError

            break

        except ValueError:
            print(LEXICON['incorrect_input'])
            continue

    count_data = int(user_input)
    print(LEXICON['manual_entry'])

    for record_number in range(1, count_data + 1):
        for cell_name in CELLS_NAME:
            while True:
                user_input = input(f'{LEXICON[cell_name]}')

                if validators['validate_exit'](user_input):
                    data.clear()
                    logging.info('Пользователь прервал ввод данных.')
                    return data

                if validators[cell_name](user_input):
                    data[cell_name].append(user_input)
                    break

                else:
                    print(LEXICON['incorrect_input'])

        print('Осталось анкет для заполнения: '
              f'{count_data - record_number}, '
              f'заполнено: {record_number}.\n')
    logging.info('Данные успешно сформированы.')
    return data


def automatic_generation() -> defaultdict | None:
    '''
    Обрабатывает ввод от пользователя необходмый для автоматической генерации
    данных.
    Взвращает словарь даннах или None если программа прервана пользователем.
    '''
    logging.info('Пользователь выбрал автоматическую генерацию.')
    print(LEXICON['automatic_entry'])

    while True:
        user_input = input(LEXICON['data_count_manual'])

        if validators['validate_exit'](user_input):
            logging.info('Пользователь прервал ввод данных.')
            return None

        if validate_count_data(user_input) or user_input == '':
            break

        print(LEXICON['incorrect_input'])
        continue

    count_data = int(user_input) if user_input else None
    data = DataGenerator(count_data)
    print(LEXICON['generate_date'])
    data.generate_data()
    logging.info('Данные успешно сформированы.')
    return data.get_data()


def archive_selection() -> int:
    '''
    Запрашивает у пользователя тип архива, в который будут упакованы файлы.
    '''
    while True:
        user_input = input(LEXICON['archive_selection'])
        if validators['validate_exit'](user_input):
            return 0

        if not validators['archive_selection'](user_input):
            print(LEXICON['incorrect_input'])
            continue

        return int(user_input)
