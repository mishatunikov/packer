from lexicon.lexicon import LEXICON


def greetings():
    start_message = input(LEXICON['greetings'])

    while True:
        try:
            result = int(start_message)
            if 1 <= result <= 3:
                ...
            else:
                raise ValueError

        except Exception:
            print()
