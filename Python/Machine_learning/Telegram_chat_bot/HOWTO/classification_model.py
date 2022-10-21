import json
import os
import urllib.request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier
import pickle


def download_dataset(filename):
    if not os.path.isfile(filename):
        url = "https://drive.google.com/uc?export=view&id=1u4sNekGHaDzgkOVzCOAbyWpFTEMfu95Z"
        urllib.request.urlretrieve(url, filename)


def get_intent(text):
    """Определяем тему по тексту от пользователя"""
    text_vec = vectorizer.transform([text])
    return model.predict(text_vec)[0]


if __name__ == '__main__':
    filename = "intents_dataset.json"
    download_dataset(filename=filename)

    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)  # Считываем json-файл, превращая его в питоновский словарь

    # Пробегаем по всему словарю - берем пары ключ-значение и раскладываем по двум спискам
    # сначала берем пары name, intent из словаря
    # потом для каждого элемента в examples и responses добавляем в X элемент,
    # а в y параллельно кладем name - название корневого интента
    X = []
    Y = []

    for intent_name in data:
        for example in data[intent_name]['examples']:
            X.append(example)
            Y.append(intent_name)
        for response in data[intent_name]['responses']:
            X.append(response)
            Y.append(intent_name)

    # Произведем векторизацию данных
    # Векторизация - процесс кодирования слова в набор чисел
    vectorizer = CountVectorizer()
    vectorizer.fit(X)
    X_vec = vectorizer.transform(X)

    # Создаем модель
    model = MLPClassifier()
    # Обучаем модель
    model.fit(X_vec, Y)

    # Оценка качества работы модели
    print(model.score(X_vec, Y))

    # Сохраним состояние модели, чтобы не обучать ее снова
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)


    # Немного теории:
    # Формула линейной регрессии f(x) = a1 * x1 + a1 * x2 + ... an * xn + b
    # X - строчки в "векторной" таблице,  xi - значения в колонках
    # обучение = подбор коэффициентов ai
    # Нейронка - это сложная комбинация таких регрессий - получается сложная формула со множеством коэффициентов
"""
    Структура словаря (намерения (темы) - интенты):
    намерение
        примеры запроса
            пример запроса
            ...
            пример запроса
        примеры ответа
            пример ответа
            ...
            пример ответа
    ...
    намерение
"""
