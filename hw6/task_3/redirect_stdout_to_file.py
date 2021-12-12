import sys


def redirect_output(filepath):
    """
    Декоратор для перевода stdout в файл
    :param filepath: путь к файлу, куда перенаправляется stdout
    """
    def decorator(function):
        def wrapper(*args, **kwargs):
            original_stdout = sys.stdout
            with open(filepath, 'a') as my_file_stdout:
                sys.stdout = my_file_stdout
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
    calculate()
