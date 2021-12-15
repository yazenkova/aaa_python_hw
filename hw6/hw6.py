from typing import Callable
import datetime
import sys

ORIGINAL_WRITE = sys.stdout.write


# задание 1
def my_write(string_text: str):
    """
    Добавление в стандартному выводу текущего времени
    :param string_text: строка для вывода
    """
    if not len(string_text.replace('\n', '')):
        return
    now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    output_row = f'[{now_str}]: {string_text}\n'
    ORIGINAL_WRITE(output_row)


# задание 2
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


# задание 3
def redirect_output(filepath):
    """
    Декоратор для перевода stdout в файл
    :param filepath: путь к файлу, куда перенаправляется stdout
    """
    def decorator(function):
        def wrapper(*args, **kwargs):
            now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            delimiter = f'function \'{function.__name__}\' at {now_str}\n'
            original_stdout = sys.stdout
            with open(filepath, 'a') as my_file_stdout:
                sys.stdout = my_file_stdout
                sys.stdout.write(delimiter)
                function(*args, **kwargs)
            sys.stdout = original_stdout
        return wrapper
    return decorator


@redirect_output('./function_output.txt')
def calculate():
    """
    Выводит степени от 1 до 4 чисел от 1 до 19
    """
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


if __name__ == '__main__':
    # задание 1
    sys.stdout.write = my_write
    print(input())
    sys.stdout.write = ORIGINAL_WRITE

    # задание 2
    print_greeting('Yana')

    # задание 3
    calculate()
