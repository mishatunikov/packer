import logging

from lexicon import LEXICON
from packer import FilePacker
from timer import time_counter
from user_handlers import (archive_selection, automatic_generation, greetings,
                           user_manual_entry)

logging.basicConfig(level=logging.DEBUG,
                    format='#{levelname} {filename} {asctime} - line {lineno}: {message}',
                    datefmt='%H:%M:%S',
                    style='{')

logger = logging.getLogger(__name__)


@time_counter
def main():
    input_selection = greetings()

    if input_selection == 1:
        data = automatic_generation()

    if input_selection == 2:
        data = user_manual_entry()

    if input_selection == 3:
        print('Здесь будет добавлена возможность чтения из файла.')
        return

    if not input_selection or not data:
        print(LEXICON['exit'])
        return

    archive_type = archive_selection()

    if not archive_type:
        print(LEXICON['exit'])
        return

    if archive_type == 1:
        logger.info('Формирование архива zip...')
        FilePacker(data).create_zip()

    elif archive_type == 2:
        logger.info('Формирование архива 7z...')
        FilePacker(data).create_7z()


if __name__ == '__main__':
    logger.info('Запуск программы...')
    main()
    logger.info('Программа завершила работу.')
