import pytest
from morse import decode


@pytest.mark.parametrize('s,exp', [
    ('... --- ... ' * 30, 'SOS' * 30),
    ('.--. -.-- - .... --- -.', 'PYTHON'),
    ('- .... .   .---- ... -   .--. .-.. .- -.-. .', 'THE 1ST PLACE'),
    ('', '')
])
def test_func(s, exp):
    """
    Тест на правильность работы decoder() на примерах
    :param s: закодированная строка, подающаяся на вход decoder()
    :param exp: ожидаемое значение
    """
    assert decode(s) == exp
