# timer.py

import logging
import time


def time_counter(func):
    def wrappers(*args, **kwargs):
        start_time = time.time()
        logging.debug(f'Функция {func.__name__} начала работу.')
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.debug(f'Функция {func.__name__} закончила работу. '
                      f'Время работы: {(end_time - start_time):.3f} ceк.')
        return result
    return wrappers