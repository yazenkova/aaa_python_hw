from unittest.mock import patch
import pytest
from what_is_year_now import what_is_year_now
from io import StringIO


def test_date_dash():
    """
    Тест на корректную работу с датой в формате 'YYYY-MM-DD'
    """
    exp_response = '{"currentDateTime": "2021-12-02T13:52Z"}'
    with patch('urllib.request.urlopen', return_value=StringIO(exp_response)):
        actual = what_is_year_now()
    expected = 2021
    assert actual == expected


def test_date_dot():
    """
    Тест на корректную работу с датой в формате 'DD.MM.YYYY'
    """
    exp_response = '{"currentDateTime": "02.12.2021T13:52Z"}'
    with patch('urllib.request.urlopen', return_value=StringIO(exp_response)):
        actual = what_is_year_now()
    expected = 2021
    assert actual == expected


def test_date_incorrect_format():
    """
    Тест на некорректный формат даты 'DD/MM/YYYY'
    """
    exp_response = '{"currentDateTime": "02/12/2021T13:52Z"}'
    with patch('urllib.request.urlopen', return_value=StringIO(exp_response)):
        with pytest.raises(ValueError):
            what_is_year_now()


def test_date_incorrect_response():
    """
    Тест на некорректный response (нет нужного ключа)
    """
    exp_response = '{"date": "02/12/2021T13:52Z"}'
    with patch('urllib.request.urlopen', return_value=StringIO(exp_response)):
        with pytest.raises(KeyError):
            what_is_year_now()


def test_incorrect_index_dot():
    """
    Тест на некорректный формат даты (без ведущих нулей)
    """
    exp_response = '{"currentDateTime": "2.3.2021T13:52Z"}'
    with patch('urllib.request.urlopen', return_value=StringIO(exp_response)):
        with pytest.raises(ValueError):
            what_is_year_now()
