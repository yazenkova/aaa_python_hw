import unittest
from one_hot_encoder import fit_transform

class TestFitTransformFunction(unittest.TestCase):
    def test_cities(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]

        self.assertEqual(fit_transform(cities), exp_transformed_cities)

    def test_zero_args(self):
        with self.assertRaises(TypeError) as context:
            fit_transform()

    def test_empty_input(self):
        self.assertEqual(fit_transform([]), [])

    def test_temperature_in(self):
        input = ['cold', 'cold', 'warm', 'cold', 'hot', 'hot', 'warm', 'cold', 'warm', 'hot']
        self.assertIn(('warm', [0, 1, 0]), fit_transform(input))

    def test_temperature_not_in(self):
        input = ['cold', 'cold', 'warm', 'cold', 'hot', 'hot', 'warm', 'cold', 'warm', 'hot']
        self.assertNotIn(('cold', [0, 1, 0]), fit_transform(input))

    def test_one_string_input(self):
        input = 'Hello world!'
        self.assertEqual(fit_transform(input), [('Hello world!', [1])])

    def test_gender_not_equal(self):
        input = ['Female', 'Female', 'Male', 'Female']
        answer = [('Female', [0, 1]), ('Female', [0, 1]), ('Male', [1, 0]), ('Female', [0, 1])]
        self.assertNotEqual(answer, fit_transform(input * 2))

if __name__ == '__main__':
    unittest.main()
