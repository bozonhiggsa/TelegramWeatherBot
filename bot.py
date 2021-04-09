# coding = utf-8
import telebot
import pyowm
from pyowm.exceptions.api_response_error import NotFoundError

import config

bot = telebot.TeleBot(config.TOKEN)
owm = pyowm.OWM(config.key_pyowm, language='ru')


@bot.message_handler(commands=['start'])
def welcome(message):
    sticker = open('static/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}\nЯ - <b>{1.first_name}</b>, бот погоды. Пришли название города.".format(
                         message.from_user, bot.get_me()), parse_mode='html')


@bot.message_handler(content_types=['text'])
def echo_method(message):
    try:
        observation = owm.weather_at_place(message.text)
        weather = observation.get_weather()
        humidity = weather.get_humidity()
        wind = weather.get_wind()['speed']
        temperature = weather.get_temperature('celsius')['temp']
        answer = 'В городе ' + message.text + ' сейчас ' + str(weather.get_detailed_status()) + ',\n'
        answer += 'температура ' + str(temperature) + ' град, влажность ' + str(humidity) + ' %,\n'
        answer += 'Скорость ветра ' + str(wind) + ' м/с.'

        bot.send_message(message.chat.id, answer)

    except NotFoundError:
        bot.send_message(message.chat.id, 'Такого города нет в базе')


# RUN
bot.polling(none_stop=True)
