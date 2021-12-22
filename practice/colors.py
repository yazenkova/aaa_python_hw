from abc_practice import ABC, abstractmethod


class Contrast:

    def __init__(self, c):
        self.c = c

    def __mul__(self, other: 'Color'):
        if not isinstance(other, Color):
            raise ValueError('not implemented')
        cl = -256 * (1 - self.c)
        F = (259 * (cl + 255)) / (255 * (259 - cl))
        return Color(int(F * (other.red - 128) + 128),
                     int(F * (other.green - 128) + 128),
                     int(F * (other.blue - 128) + 128)
                     )


class ComputerColor(ABC):
    """Abstract class"""

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __rmul__(self, other):
        pass


class Color(ComputerColor):
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red: int, green: int, blue: int):
        if red > 255 or green > 255 or blue > 255:
            raise ValueError('color must be <= 255')
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return f'{self.START};{self.red};{self.green};' \
               f'{self.blue}{self.MOD}●{self.END}{self.MOD}'

    def __repr__(self):
        return str(self)

    def __eq__(self, other: 'Color'):
        if isinstance(other, Color):
            return self.red == other.red and \
                   self.green == other.green and \
                   self.blue == other.blue
        else:
            return False

    def __add__(self, other: 'Color'):
        return Color(self.red + other.red,
                     self.green + other.green,
                     self.blue + other.blue
                     )

    def __hash__(self):
        return hash((self.red, self.green, self.red))

    def __mul__(self, c: float):
        if 0 > c > 1:
            raise ValueError('c must be in range(0, 1)')
        contrast = Contrast(c)
        return contrast.__mul__(self)

    __rmul__ = __mul__


if __name__ == '__main__':
    red = Color(255, 0, 0)
    print(red)
