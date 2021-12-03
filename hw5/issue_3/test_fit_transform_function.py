import unittest
from one_hot_encoder import fit_transform


class TestFitTransformFunction(unittest.TestCase):
    def test_cities(self):
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
        self.assertEqual(fit_transform(cities), exp_transformed_cities)

    def test_zero_args(self):
        """
        Тест на отсутствие аргументов (ловим исключение)
        """
        with self.assertRaises(TypeError):
            fit_transform()

    def test_empty_input(self):
        """
        Тест на пустой вход
        """
        self.assertEqual(fit_transform([]), [])

    def test_temperature_in(self):
        """
        Тест на проверку вхождения одного из значений в ответ
        """
        inp = ['cold', 'cold', 'warm', 'cold', 'hot', 'hot',
               'warm', 'cold', 'warm', 'hot']
        self.assertIn(('warm', [0, 1, 0]), fit_transform(inp))

    def test_temperature_not_in(self):
        """
        Тест на проверку отстутсвия закодированного значения в ответе
        """
        inp = ['cold', 'cold', 'warm', 'cold', 'hot', 'hot',
               'warm', 'cold', 'warm', 'hot']
        self.assertNotIn(('cold', [0, 1, 0]), fit_transform(inp))

    def test_one_string_input(self):
        """
        Тест с одним аргументом в виде str на входе
        """
        inp = 'Hello world!'
        self.assertEqual([('Hello world!', [1])], fit_transform(inp))

    def test_gender_not_equal(self):
        """
        Тест на несовпадение с некорректным ответом
        """
        inp = ['Female', 'Female', 'Male', 'Female']
        answer = [('Female', [1, 0]),
                  ('Female', [0, 1]),
                  ('Male', [1, 0]),
                  ('Female', [0, 1])]
        self.assertNotEqual(fit_transform(inp), answer)


if __name__ == '__main__':
    unittest.main()
