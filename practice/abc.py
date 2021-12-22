import random
from abc import ABC, abstractmethod


class AnimeMon(ABC):

    def __init__(self):
        self._exp = 0

    @property
    @abstractmethod
    def exp(self) -> int:
        """
        :return: значение опыта
        """
        return self._exp

    @abstractmethod
    def inc_exp(self, value: int):
        """Метод увеличения опыта"""


class Pokemon(AnimeMon):
    @property
    def exp(self) -> int:
        return super().exp

    def inc_exp(self, value: int) -> None:
        self._exp += value * 4


class Digimon(AnimeMon):
    @property
    def exp(self) -> int:
        return super().exp

    def inc_exp(self, value: int):
        self._exp += value * 8


def train(warrior: AnimeMon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - warrior.exp % level_size) // step_size
    for _ in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            warrior.inc_exp(step_size)


if __name__ == '__main__':
    pokemon = Pokemon()
    digimon = Digimon()
    assert pokemon.exp == 0 and digimon.exp == 0, 'Wrong init'
    train(digimon)
    print(f'Digimon exp is {digimon.exp}')
    train(pokemon)
    print(f'Pokemon exp is {pokemon.exp}')
