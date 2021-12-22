from typing import List
from collections import defaultdict
from math import log


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


class TfidfTransformer:
    """Tfidf преобразование"""

    @staticmethod
    def tf_transform(count_matrix: List[List[int]]) -> List[List[float]]:
        """
        Подсчет tf-матрицы
        :param count_matrix: веткорное представление всех предложенй
        :return: tf-матрица
        """
        tf_matrix_out = []
        for vector in count_matrix:
            tf_matrix_out.append([freq / sum(vector) for freq in vector])
        return tf_matrix_out

    @staticmethod
    def idf_transform(count_matrix: List[List[int]]) -> List[float]:
        """
        Подсчет idf-матрицы
        :param count_matrix: веткорное представление всех предложенй
        :return: idf-матрица
        """
        vector_idf_transform = []
        zip_generator_col = zip(*count_matrix)
        for _ in range(len(count_matrix[0])):
            current_sum = sum([1 for x in next(zip_generator_col) if x])
            vector_idf_transform.append(log((len(count_matrix) + 1)
                                            / (current_sum + 1)) + 1)
        return vector_idf_transform

    def fit_transform(self, count_matrix: List[List[int]]) \
            -> List[List[float]]:
        """
        Подсчет tf-idf матрицы
        :param count_matrix: веткорное представление всех предложенй
        :return: tf-idf матрица
        """
        tf_matrix = self.tf_transform(count_matrix)
        idf_matrix = self.idf_transform(count_matrix)
        tf_idf_matrix = []
        for vector in tf_matrix:
            current_vector = []
            zipped_vector_col = zip(vector, idf_matrix)
            for tf, idf in zipped_vector_col:
                current_vector.append(tf * idf)
            tf_idf_matrix.append(current_vector)
        return tf_idf_matrix


class TfifdVectorizer(CountVectorizer):
    """TfIdf преобразование исходного корпуса документов"""

    def __init__(self):
        super().__init__()
        self.tfidf = TfidfTransformer()

    def fit_transform(self, text_corpus: List[str]) -> List[List[float]]:
        count_matrix = super().fit_transform(text_corpus)
        return self.tfidf.fit_transform(count_matrix)


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfifdVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(count_matrix)
