import json
import os
import time
import urllib.request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier
import pickle
import random

start = time.time()

def get_response(text, data):
    text_vec = vectorizer.transform([text])
    intent = model.predict(text_vec)[0]
    return random.choice(data[intent]['responses'])

with open('model.pkl', 'br') as f:
    model = pickle.load(f)
filename = "intents_dataset.json"


with open(filename, 'r', encoding='utf-8') as f:
    data = json.load(f)  # Считываем json-файл, превращая его в питоновский словарь
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

launch_time = time.time() - start
print(f'Нейронка запустилась за {launch_time}')
while True:
    print(get_response(text=input(), data=data))

