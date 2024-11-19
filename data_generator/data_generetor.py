from collections import defaultdict, deque
from concurrent.futures import ProcessPoolExecutor
from random import randint

from mimesis import Generic
from mimesis.locales import Locale

from timer import time_counter


class DataGenerator:
    """
    Класс - генератор данных.
    Генерирует данные с помощью библиотеки mimesis.
    """

    def __init__(self, data_count: int | None = None) -> None:
        self._mimes = Generic(Locale.RU, seed=None)
        self.data: defaultdict = defaultdict(deque)
        if not data_count:
            data_count = randint(500_000, 2_500_000)
        self._data_count: int = data_count

    def generate_names(self) -> list:
        '''Генерирует имена с помощью библиотеки mimesis.'''
        return [self._mimes.person.full_name() for _ in range(self._data_count)]

    def generate_date_of_birthdays(self) -> list:
        '''Генерирует даты рождения с помощью библиотеки mimesis.'''
        return [self._mimes.person.birthdate(
                min_year=1940, max_year=2006).strftime('%d.%m.%Y')
                for _ in range(self._data_count)]

    def generate_usernames(self) -> list:
        '''Генерирует usernames с помощью библиотеки mimesis.'''
        return [f'@{self._mimes.person.username()}'
                for _ in range(self._data_count)]

    def generate_jobs(self) -> list:
        '''Генерирует профессии с помощью библиотеки mimesis.'''
        return [self._mimes.person.occupation()
                for _ in range(self._data_count)]

    def generate_work_companies(self) -> list:
        '''Генерирует места работы с помощью библиотеки mimesis.'''
        return [self._mimes.finance.company()
                for _ in range(self._data_count)]

    def generate_post_indexs(self) -> list:
        '''Генерирует почтовые индексы с помощью библиотеки mimesis.'''
        return [self._mimes.address.postal_code()
                for _ in range(self._data_count)]

    def generate_cities(self) -> list:
        '''Генерирует города с помощью библиотеки mimesis.'''
        return [self._mimes.address.city() for _ in range(self._data_count)]

    def generate_health_category(self) -> list:
        '''Генерирует группы здоровья с помощью библиотеки mimesis.'''
        return [self._mimes.random.randint(1, 3)
                for _ in range(self._data_count)]

    def generate_phones(self) -> list:
        '''Генерирует номера телефонов с помощью библиотеки mimesis.'''
        return [self._mimes.person.phone_number(mask='8##########')
                for _ in range(self._data_count)]

    def generate_emails(self) -> list:
        '''Генерирует адреса электронной почты с помощью библиотеки mimesis.'''
        return [self._mimes.person.email() for _ in range(self._data_count)]

    @time_counter
    def generate_data(self) -> None:
        '''
        Генерирует данные и добавляет их в словарь data.
        Если данным экземпляром класса ранее была произведена
        генерация, то новые данные будут добавлены к
        старым. Для очистки словаря используйте метод clear_data.
        '''
        # if self._data_count > 10000:
        #     with ProcessPoolExecutor() as pool:
        #         result: list = [
        #             ('ФИО', pool.submit(self.generate_names)),
        #             ('Дата рождения',
        #              pool.submit(self.generate_date_of_birthdays)),
        #             ('Категория здоровья',
        #              pool.submit(self.generate_health_category)),
        #             ('Почтовый индекс',
        #              pool.submit(self.generate_post_indexs)),
        #             ('Город', pool.submit(self.generate_cities)),
        #             ('Профессия', pool.submit(self.generate_jobs)),
        #             ('Место работы',
        #              pool.submit(self.generate_work_companies)),
        #             ('Имя пользователя', pool.submit(self.generate_usernames)),
        #             ('Электронная почта', pool.submit(self.generate_emails)),
        #             ('Номер телефона', pool.submit(self.generate_phones)),
        #         ]

        #         for column_name, info in result:
        #             self.data[column_name].extend(info.result())
        # else:
        self.data['ФИО'] = self.generate_names()
        self.data['Дата рождения'] = self.generate_date_of_birthdays()
        self.data['Категория здоровья'] = self.generate_health_category()
        self.data['Почтовый индекс'] = self.generate_post_indexs()
        self.data['Город'] = self.generate_cities()
        self.data['Профессия'] = self.generate_jobs()
        self.data['Место работы'] = self.generate_work_companies()
        self.data['Имя пользователя'] = self.generate_usernames()
        self.data['Электронная почта'] = self.generate_emails()
        self.data['Номер телефона'] = self.generate_phones()

    def get_data(self):
        '''Возращает словарь сгенерированных данных.'''
        return self.data

    def clear_data(self) -> None:
        '''Очищает data от существующих записей'''
        self.data.clear()
