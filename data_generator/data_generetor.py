import time
from collections import defaultdict, deque
from concurrent.futures import ProcessPoolExecutor
from random import randint

from faker import Faker


class DataGenerator:
    """Класс - генератор данных."""

    def __init__(self, data_count: int | None = None) -> None:
        self._fake = Faker(locale='ru_RU')
        self.data: defaultdict = defaultdict(deque)
        if not data_count:
            data_count = randint(500_000, 2_500_000)
        self._data_count = data_count

    def generate_names(self) -> list:
        '''Генерирует имена с помощью библиотеки faker.'''
        return [self._fake.name() for _ in range(self._data_count)]

    def generate_date_of_birthdays(self) -> list:
        '''Генерирует даты рождения с помощью библиотеки faker.'''
        return [self._fake.date_of_birth(minimum_age=17, maximum_age=80)
                for _ in range(self._data_count)]

    def generate_usernames(self) -> list:
        '''Генерирует usernames с помощью библиотеки faker.'''
        return [self._fake.user_name() for _ in range(self._data_count)]

    def generate_jobs(self) -> list:
        '''Генерирует профессии с помощью библиотеки faker.'''
        return [self._fake.job() for _ in range(self._data_count)]

    def generate_work_companies(self) -> list:
        '''Генерирует места работы с помощью библиотеки faker.'''
        return [self._fake.company() for _ in range(self._data_count)]

    def generate_post_indexs(self) -> list:
        '''Генерирует почтовые индексы с помощью библиотеки faker.'''
        return [self._fake.postcode() for _ in range(self._data_count)]

    def generate_cities(self) -> list:
        '''Генерирует города с помощью библиотеки faker.'''
        return [self._fake.city() for _ in range(self._data_count)]

    def generate_steet_addess(self) -> list:
        '''Генерирует адреса улиц с помощью библиотеки faker.'''
        return [self._fake.street_address() for _ in range(self._data_count)]

    def generate_phones(self) -> list:
        '''Генерирует номера телефонов с помощью библиотеки faker.'''
        return [self._fake.phone_number() for _ in range(self._data_count)]

    def generate_emails(self) -> list:
        '''Генерирует адреса электронной почты с помощью библиотеки faker.'''
        return [self._fake.email() for _ in range(self._data_count)]

    def generate_data(self) -> defaultdict[str, list]:
        """
        Возращает словарь данных, сгенерированный всеми функциями класса
        DataGeneretor. Если данных экземпляром класса была ранее произведена
        генерация функцией generate_data, то новые данные будут добавлены к
        старым. Для очистки словаря используйте метод clear_data.
        """
        with ProcessPoolExecutor() as pool:
            result: list = [
                ('ФИО', pool.submit(self.generate_names)),
                ('Дата рождения',
                 pool.submit(self.generate_date_of_birthdays)),
                ('Почтовый индекс', pool.submit(self.generate_post_indexs)),
                ('Город', pool.submit(self.generate_cities)),
                ('Улица', pool.submit(self.generate_steet_addess)),
                ('Профессия', pool.submit(self.generate_jobs)),
                ('Место работы', pool.submit(self.generate_work_companies)),
                ('Имя пользователя', pool.submit(self.generate_usernames)),
                ('Электронная почта', pool.submit(self.generate_emails)),
                ('Номер телефона', pool.submit(self.generate_phones)),
            ]

            for column_name, info in result:
                self.data[column_name].extend(info.result())

        return self.data

    def clear_data(self) -> None:
        self.data.clear()
