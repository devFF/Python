import json
from sklearn.feature_extraction.text import CountVectorizer
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters
import pickle
import random


async def text_reply(upd: Update, ctx):
    user_text = upd.message.text
    print(f'User: {user_text}')
    answer = get_response(text=user_text)
    await upd.message.reply_text(answer)


def load_model():
    print('Загрузка модели')
    with open('model.pkl', 'br') as f:
        return pickle.load(f)


def load_dataset(filename):
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

    vectorizer = CountVectorizer()
    vectorizer.fit(X)
    X_vec = vectorizer.transform(X)
    return data, vectorizer, X_vec


def get_response(text):
    text_vec = vectorizer.transform([text])
    intent = model.predict(text_vec)[0]
    return random.choice(data[intent]['responses'])


if __name__ == '__main__':
    # Загрузка нейронки
    model = load_model()
    # Загрузка ответов и векторизация
    data, vectorizer, X_vec = load_dataset(filename='intents_dataset.json')

    # token - секретный ключ к боту, получить у @BotFather
    TOKEN = input('> Введите токен Вашего бота:')
    app = ApplicationBuilder().token(TOKEN).build()

    # обработчик сообщений
    handler = MessageHandler(filters.TEXT, text_reply)

    # прикрепляем обработчик к приложению
    app.add_handler(handler)

    # запуск приложения
    app.run_polling()
