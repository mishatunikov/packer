
INFO = ['ФИО',
        'Дата рождения',
        'Почтовый индекс',
        'Город',
        'Улица',
        'Профессия',
        'Место работы',
        'Имя пользователя',
        'Электронная почта',
        'Номер телефона']

LEXICON = {
    'greetings': 'Привет!\nЯ создаю информационный архив zip из файлов'
    'excel/csv/txt. Каждый файл состоит из 10 колонок информации о человеке:'
    f'{", ".join(INFO)}. Данные могут генерироваться автоматически,'
    'ручным вводом или из файла txt.\n'
    'Введи цифру от 1 до 3 для выбора способа ввода:\n'
    '1 - автоматическая генерация'
    '2 - ручной ввод'
    '3 - из файла txt'
}