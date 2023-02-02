import telebot
from telebot import types
from constants import constants, message_constants
from horoscope import Horoscope

bot = telebot.TeleBot(constants.TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b_author = types.KeyboardButton('Автор бота')
    b_signs = types.KeyboardButton('Все знаки зодиака')
    marcup.add(b_author, b_signs)
    bot.send_message(message.chat.id, message_constants.GREETINGS, reply_markup=marcup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Автор бота':
            bot.send_message(message.chat.id, message_constants.AUTHOR)
        elif message.text == 'Все знаки зодиака':
            marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            aquarius = types.KeyboardButton('Водолей(Aquarius)')
            signarius = types.KeyboardButton('Стрелец(Signarius)')
            libra = types.KeyboardButton('Весы(Libra)')
            virgo = types.KeyboardButton('Дева(Virgo)')
            back = types.KeyboardButton('Назад')
            main = types.KeyboardButton('Главное меню')
            marcup.add(aquarius, signarius, libra, virgo, back, main)
            bot.send_message(message.chat.id, 'Знаки зодиака', reply_markup=marcup)
        elif message.text == 'Назад':
            marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            aquarius = types.KeyboardButton('Водолей(Aquarius)')
            signarius = types.KeyboardButton('Стрелец(Signarius)')
            libra = types.KeyboardButton('Весы(Libra)')
            virgo = types.KeyboardButton('Дева(Virgo)')
            back = types.KeyboardButton('Назад')
            marcup.add(aquarius, signarius, libra, virgo, back)
            bot.send_message(message.chat.id, 'Знаки зодиака', reply_markup=marcup)
        elif message.text == 'Главное меню':
            marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            b_author = types.KeyboardButton('Автор бота')
            b_signs = types.KeyboardButton('Все знаки зодиака')
            marcup.add(b_author, b_signs)
            bot.send_message(message.chat.id, 'Главное меню', reply_markup=marcup)
        elif message.text == 'Водолей(Aquarius)':
            marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            b_back = types.KeyboardButton('Назад')
            b_main = types.KeyboardButton('Главное меню')
            marcup.add(b_back, b_main)
            bot.send_message(message.chat.id, Horoscope.aquarius_prediction(), reply_markup=marcup)
        elif message.text == 'Стрелец(Signarius)':
            marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            b_back = types.KeyboardButton('Назад')
            b_main = types.KeyboardButton('Главное меню')
            marcup.add(b_back, b_main)
            bot.send_message(message.chat.id, Horoscope.saginarius_prediction(), reply_markup=marcup)
        elif message.text == 'Весы(Libra)':
            marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            b_back = types.KeyboardButton('Назад')
            b_main = types.KeyboardButton('Главное меню')
            marcup.add(b_back, b_main)
            bot.send_message(message.chat.id, Horoscope.libra_prediction(), reply_markup=marcup)
        elif message.text == 'Дева(Virgo)':
            marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            b_back = types.KeyboardButton('Назад')
            b_main = types.KeyboardButton('Главное меню')
            marcup.add(b_back, b_main)
            bot.send_message(message.chat.id, Horoscope.virgo_prediction(), reply_markup=marcup)


@bot.message_handler(content_types=['text'])
def aquarius_prediction(message):
    pass


if __name__ == '__main__':
    bot.polling(none_stop=True)