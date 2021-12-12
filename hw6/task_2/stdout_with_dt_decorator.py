import datetime
import sys
from typing import Callable


def timed_output(func: Callable) -> Callable:
    """
    Добавление вывода текущего времени к работе функции
    :param func: функция, к которой применяется декоратор
    """
    def wrapper(*args, **kwargs):
        now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        output_row = f"[{now_str}]: "
        sys.stdout.write(output_row)
        return func(*args, **kwargs)

    return wrapper


@timed_output
def print_greeting(name: str):
    """
    Вывод приветствия пользователю
    :param name: имя пользователя
    """
    print(f'Hello, {name}!')


if __name__ == '__main__':
    print_greeting(input('Enter your name!\n'))
