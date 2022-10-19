from telegram import Update  # Update -- кусок информации, полученный от телеграма
from telegram.ext import ApplicationBuilder, MessageHandler, filters  # Способ создать приложение с указанием настроек


# token - секретный ключ к боту, получить у @BotFather
app = ApplicationBuilder().token('5651820426:AAEtEE_ZhpmW9l-OTXc0VTRHSF5qnICnjO8').build()

# upd - новая информация
# ctx - контекст, служебная информация
# После двоеточия тип данных
def text_reply(upd: Update, ctx):
    pass


# обработчик сообщений
handler = MessageHandler(filters.TEXT, text_reply)

# прикрепляем обработчик к приложению
app.add_handler(handler)

# запуск приложения
app.run_polling()









