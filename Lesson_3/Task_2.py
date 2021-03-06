from time import sleep


def redo_decorator(call_count, start_sleep_time, factor, border_sleep_time, func):
    def wrapper(*args, **kwargs):
        timer = start_sleep_time

        for i in range(call_count):
            if timer < border_sleep_time:
                timer = start_sleep_time * factor ** i  # надеюсь, правильно понял формулу, ибо были неясности
            if timer >= border_sleep_time:
                timer = border_sleep_time

            sleep(timer)
            result = func(*args, **kwargs)
            number = i + 1

            print(f'Запуск номер {number}. Ожидание: {timer} секунд. Результат декорируемой функций = {result}')

            wrapper.__name__ = func.__name__  # явно сохраняем имя функции
            wrapper.__doc__ = func.__doc__  # явно сохраняем описание функции

    return wrapper


def say_hello_to_my_little_friends_general_kenobi():
    """Answer to General Grievous."""
    return 'Hello there!'


# --------------------- Main ---------------------
if __name__ == '__main__':
    new_func = redo_decorator(4, 1, 2, 7, say_hello_to_my_little_friends_general_kenobi)
    new_func()

    print('\n--------------------- Some info ---------------------')
    print(new_func.__name__)
    print(new_func.__doc__)
