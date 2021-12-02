import pytest

from morse import decode


def test_sos():
    assert decode('... --- ...') == 'SOS'


def test_empty():
    assert decode('') == ''


@pytest.mark.parametrize('s,exp', [
    ('... --- ... ' * 30, 'SOS' * 30),
    ('.--. -.-- - .... --- -.', 'PYTHON'),
    ('- .... .   .---- ... -   .--. .-.. .- -.-. .', 'THE 1ST PLACE')
])
def test_func(s, exp):
    assert decode(s) == exp
