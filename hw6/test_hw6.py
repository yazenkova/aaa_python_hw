import datetime
from unittest.mock import patch
from io import StringIO
import os
from freezegun import freeze_time
from hw6 import print_greeting, calculate


@freeze_time("2021-12-10 21:00:00")
def test_timed_output():
    """
    Тест на работу декоратора @timed_output
    """
    with patch('sys.stdout', new=StringIO()) as fake_stdout:
        with patch('builtins.input', return_value='Yana'):
            print_greeting(input())
            assert fake_stdout.getvalue() == '[2021-12-10 21:00:00]:' \
                                             ' Hello, Yana!\n'


@freeze_time("2021-12-10 21:00:00")
def test_redirect_output():
    """
    Тест на работу декоратора @redirect_output
    """
    filepath = './function_output.txt'
    if os.path.exists(filepath):
        os.remove(filepath)
    calculate()
    with open(filepath, 'r') as test_output:
        content = test_output.read()

    expected_content =\
        'function \'calculate\' at 2021-12-10 21:00:00\n' \
        '1 2 3 4 5 6 7 8 9 10 11 ' \
        '12 13 14 15 16 17 18 19 \n' \
        '1 4 9 16 25 36 49 64 81 100 121' \
        ' 144 169 196 225 256 289 324 361 \n' \
        '1 8 27 64 125 216 343 512 729 1000 1331 ' \
        '1728 2197 2744 3375 4096 4913 5832 6859 \n' \
        '1 16 81 256 625 1296 2401 4096 6561 10000 14641 ' \
        '20736 28561 38416 50625 65536 83521 104976 130321 \n'

    assert content == expected_content
    os.remove(filepath)
