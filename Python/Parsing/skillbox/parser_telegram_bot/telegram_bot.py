from telegram import Update  # Update -- кусок информации, полученный от телеграма
from telegram.ext import ApplicationBuilder, MessageHandler, filters  # Способ создать приложение с указанием настроек
from head_hunter import launch_parser

# token - секретный ключ к боту, получить у @BotFather
TOKEN = input('> Введите токен Вашего бота:')
app = ApplicationBuilder().token(TOKEN).build()


# upd - новая информация
# ctx - контекст, служебная информация
# После двоеточия тип данных
async def text_reply(upd: Update, ctx):
    user_text = upd.message.text
    print(f'User: {user_text}')
    # Запуск парсинга
    name = upd.message.from_user.full_name
    answer = f'Уважаемый, {name}, мы получили Ваш запрос "{user_text}"'
    await upd.message.reply_text(answer)
    count = launch_parser(title=user_text)
    answer = f'Найдено {count} вакансий'
    await upd.message.reply_text(answer)

# Загрузка нейронки и словаря


# обработчик сообщений
handler = MessageHandler(filters.TEXT, text_reply)

# прикрепляем обработчик к приложению
app.add_handler(handler)

# запуск приложения
app.run_polling()
