import telebot
from telebot import types
token = ""
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь научиться спидраннингу?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею: \n' 
                                      '/speedrun - ссылка на главный сайт по спидраннингу. \n'
                                      '/razbor - разборы различных спидранов. \n'
                                      'начать - напиши, чтобы узнать, какой старт выбрать. \n'
                                      'игры - напиши, чтобы узнать актуальные игры для пробежки.')


@bot.message_handler(commands=['speedrun'])
def start_message(message):
    bot.send_message(message.chat.id, 'https://speedrun.com/ - тут собрано все комунити бегунов')


@bot.message_handler(commands=['razbor'])
def start_message(message):
    bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=7dtLKwdNwgI&list=PLEC96c5s5BGVObuj0qpzLGAS5AgTiDMDu '
                                      'Плейлист с разборчиками по интересным играм')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "начать":
        bot.send_message(message.chat.id, 'Для начала тебе потребуется упорство, много упорства, надеюсь ты готов прыгать на коробки по 10 часов в день ради результата, самое простое - взять какую-либо старую игру, которую уже довольно сильно изучили, посмотреть актуальные спидраны на сайте speedrun.com, а дальше все в твоих руках')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "игры":
        bot.send_message(message.chat.id, 'Сюда бы добавить какие-то актуальные, но пока бегай в то, что нравится')


if __name__ == '__main__':
    bot.infinity_polling()
