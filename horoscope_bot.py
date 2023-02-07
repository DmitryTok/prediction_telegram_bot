import telebot
from telebot import types
from constants import constants, message_constants, buttons
from horoscope import Horoscope


bot = telebot.TeleBot(constants.TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    marcup = types.ReplyKeyboardMarkup()
    marcup.add(
        buttons.B_AUTHOR,
        buttons.B_SIGNS
    )
    bot.send_message(message.chat.id, message_constants.GREETINGS, reply_markup=marcup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    marcup = types.ReplyKeyboardMarkup()
    if message.chat.type == 'private':
        if message.text == 'Автор бота':
            bot.send_message(message.chat.id, message_constants.AUTHOR)
        elif message.text == 'Все знаки зодиака':
            marcup.add(
                buttons.B_VIGRO,
                buttons.B_AQUARIUS,
                buttons.B_SIGNARIUS,
                buttons.B_LIBRA,
                buttons.B_MAIN
            )
            bot.send_message(message.chat.id, 'Знаки зодиака', reply_markup=marcup)
        elif message.text == 'Назад':
            marcup.add(
                buttons.B_VIGRO,
                buttons.B_AQUARIUS,
                buttons.B_SIGNARIUS,
                buttons.B_LIBRA,
                buttons.B_MAIN
            )
            bot.send_message(message.chat.id, 'Знаки зодиака', reply_markup=marcup)
        elif message.text == 'Главное меню':
            marcup.add(
                buttons.B_AUTHOR,
                buttons.B_SIGNS
            )
            bot.send_message(message.chat.id, 'Главное меню', reply_markup=marcup)
        elif message.text == 'Водолей(Aquarius)':
            marcup.add(
                buttons.B_BACK,
                buttons.B_MAIN
            )
            bot.send_message(message.chat.id, Horoscope.aquarius_prediction(), reply_markup=marcup)
        elif message.text == 'Стрелец(Signarius)':
            marcup.add(
                buttons.B_BACK,
                buttons.B_MAIN
            )
            bot.send_message(message.chat.id, Horoscope.saginarius_prediction(), reply_markup=marcup)
        elif message.text == 'Весы(Libra)':
            marcup.add(
                buttons.B_BACK,
                buttons.B_MAIN
            )
            bot.send_message(message.chat.id, Horoscope.libra_prediction(), reply_markup=marcup)
        elif message.text == 'Дева(Virgo)':
            marcup.add(
                buttons.B_BACK,
                buttons.B_MAIN
            )
            bot.send_message(message.chat.id, Horoscope.virgo_prediction(), reply_markup=marcup)


if __name__ == '__main__':
    bot.polling(none_stop=True)
