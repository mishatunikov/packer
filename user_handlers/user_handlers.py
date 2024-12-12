import logging
from collections import defaultdict, deque


from data_generator import DataGenerator
from lexicon import CELLS_NAME, LEXICON
from packer.constants import SUPPORTED_FORMATS
from packer.validators import validators, validate_count_data


def greetings() -> int:
    """
    Выводит стартовое сообщение для пользователя и
    запрашивает выбор ввода от него.
    """
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


def user_manual_entry() -> defaultdict[str, deque]:
    """
    Обрабатывает ручной ввод от пользователя.
    Возвращает словарь, состоящий из введенных данных.
    """
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
    """
    Обрабатывает ввод от пользователя необходимый для автоматической генерации
    данных.
    Возвращает словарь данных или None если программа прервана пользователем.
    """
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
    """
    Запрашивает у пользователя тип архива, в который будут упакованы файлы.
    """
    while True:
        user_input = input(LEXICON['archive_selection'])
        if validators['validate_exit'](user_input):
            return 0

        if not validators['archive_selection'](user_input):
            print(LEXICON['incorrect_input'])
            continue

        return int(user_input)


def format_selection():
    """
    Запрашивает у пользователя формат данных и возвращает результат выбора.
    """
    logging.info('Пользователь выбирает формат данных.')
    print(LEXICON['format_selection'])
    while True:
        user_input = input()
        if validators['validate_exit'](user_input):
            return 0

        if not validators['validate_format_selection'](user_input):
            print(LEXICON['incorrect_input'])
            continue

        selected_formats = tuple(SUPPORTED_FORMATS[format_number] for format_number in user_input)
        logging.info(f'Пользователь выбрал форматы: {selected_formats}.')
        return selected_formats
