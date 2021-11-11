import json
from keyword import iskeyword


class Parser:
    """
    Класс-парсер словаря в объект с доступами
    к значениям через атрибуты
    """

    def __init__(self, data_dict: dict):
        for key, value in data_dict.items():
            if iskeyword(key):
                key += '_'
            if isinstance(value, dict):
                self.__dict__[key] = Parser(value)
            else:
                self.__dict__[key] = value


class ColorizeMixin:
    """
    Миксин для представления объявления с изменением цвета
    """
    repr_color_code = 32

    def __str__(self):
        text_advert = self.__repr__()
        return f'\033[0;{self.repr_color_code}m' + text_advert


class Advert(ColorizeMixin, Parser):
    """
    Класс объявлений, который по словарю на входе
    производит парсинг и сохраняет все значения в атрибуты объекта класса.
    Есть обязательное условие на неотрицательность цены в объявлении.
    """

    def __init__(self, data_dict: dict):
        self.price = 0
        self.title = ''
        super(Advert, self).__init__(data_dict)
        if self.price < 0:
            raise ValueError('price must be >= 0')

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


if __name__ == '__main__':
    data = """{
    "title": "Вельш-корги",
    "price": 1000,
    "class": "dogs",
    "location": {
    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
    }
    }"""

    data_d = json.loads(data)

    try:
        adv = Advert(data_d)
        print(adv)
        print(adv.class_, adv.price, adv.location.address)
    except ValueError:
        print('ValueError: price must be >= 0. Try again')
