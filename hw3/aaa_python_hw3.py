from typing import List
from collections import defaultdict


class CountVectorizer():
    """
    Класс, который переводит набор предложений в
    матрицу векторов с подсчитанными значениями токенов.
    """

    def __init__(self):
        self.count_matrix = []
        self.features = defaultdict(int)
        self.features_names = []
        self.sentence_freqs = []

    def _read_sentence(self, sentence: str) -> defaultdict:
        """
        Чтение предложения, подсчет частот вхождения токенов
        и добавление их в общий набор
        :param sentence - предложение
        """
        words_freq = defaultdict(int)
        for word in sentence.lower().split():
            words_freq[word] += 1
            self.features[word] += 1
        return words_freq

    def _fit(self, corpus: List[str]) -> None:
        """
        Из корпуса предложений выделяем токены
        и производим их подсчет в каждом предложении.
        :param corpus - list предложений
        """
        self.count_matrix = []
        self.features = defaultdict(int)
        self.sentence_freqs = []

        for sentence in corpus:
            self.sentence_freqs.append(self._read_sentence(sentence))
        self.features_names = list(self.features.keys())

    def _transform(self) -> List[List[int]]:
        """
        По подсчитанным частотам вхождения токенов
        строим векторное представление предложений
        :return: веткорное представление всех предложенй
        """
        for sentence_freq in self.sentence_freqs:
            sentence_vector = []
            for feature in self.features:
                sentence_vector.append(sentence_freq[feature])
            self.count_matrix.append(sentence_vector)
        return self.count_matrix

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """
        Объединение _fit и _transform, извлекаем токены
        и над ними строим векторное представление набора предложений
        :return: веткорное представление всех предложенй
        """
        self._fit(corpus)
        return self._transform()

    def get_feature_names(self) -> List[str]:
        """
        Возвращает список токенов в порядке их чтения
        в наборе предложений.
        :return: список токенов
        """
        if len(self.features_names) == 0:
            print('Список токенов пуст, для начала вызовите fit_transform()')
            return
        return self.features_names


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    assert count_matrix == [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    print(count_matrix)
    feature_list = vectorizer.get_feature_names()
    assert feature_list == ['crock', 'pot', 'pasta', 'never', 'boil',
                            'again', 'pomodoro', 'fresh', 'ingredients',
                            'parmesan', 'to', 'taste']
    print(feature_list)
