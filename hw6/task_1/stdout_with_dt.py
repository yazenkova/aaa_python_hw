import datetime
import sys

ORIGINAL_WRITE = sys.stdout.write


def my_write(string_text: str):
    """
    Добавление в стандартному выводу текущего времени
    :param string_text: строка для вывода
    """
    if not len(string_text.rstrip('\n')):
        return
    now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    output_row = f'[{now_str}]: {string_text}\n'
    ORIGINAL_WRITE(output_row)


if __name__ == '__main__':
    sys.stdout.write = my_write
    print(input())
    sys.stdout.write = ORIGINAL_WRITE
