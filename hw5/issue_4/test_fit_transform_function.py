import pytest
from one_hot_encoder import fit_transform


def test_cities():
    """
    Тест на примере из исходного кода
    """
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert fit_transform(cities) == exp_transformed_cities


def test_zero_args():
    """
    Тест на отсутствии аргументов (ловим исключение)
    """
    with pytest.raises(TypeError):
        fit_transform()


@pytest.mark.parametrize('s,exp', [
    (
            ['cold', 'cold', 'warm', 'cold',
             'hot', 'hot', 'warm', 'cold',
             'warm', 'hot'],
            ('warm', [0, 1, 0])
    ),
    (
            ['Female', 'Female', 'Male', 'Female'],
            ('Female', [0, 1])
    )
])
def test_result_in(s, exp):
    """
    Тест на вхождение правильной кодировки слова в ответ
    :param s: исходный набор строк
    :param exp: ожидаемая кодировка одного из слов
    """
    assert exp in fit_transform(s)


@pytest.mark.parametrize('s,exp', [
    (
            'Hello world!',
            [('Hello world!', [1])]
    ),
    (
            ['Female', 'Female', 'Male', 'Female'],
            [('Female', [0, 1]),
             ('Female', [0, 1]),
             ('Male', [1, 0]),
             ('Female', [0, 1])]
    ),
    (
            [],
            []
    )
])
def test_result_equal(s, exp):
    """
    Тест на соответствие кодировки правильному ответу
    :param s: исходный набор строк
    :param exp: ожидаемая кодировка исходного набора
    """
    assert fit_transform(s) == exp
