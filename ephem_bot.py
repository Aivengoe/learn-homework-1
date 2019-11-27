"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
from settings import tele_token, PROXY
from datetime import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 

def  planet_constellation(bot, update):
    user_text = update.message.text
    planet =  user_text.split()[1]
    to_day = datetime.today()
    data_day = "{year}/{month}/{day}".format(year = to_day.year, month = to_day.month, day = to_day.day) 
    
    planets_dict ={
        'Mercury': ephem.Mercury(data_day),
        'Venus': ephem.Venus(data_day),
        'Mars': ephem.Mars(data_day),
        'Jupiter': ephem.Jupiter(data_day),
        'Saturn': ephem.Saturn(data_day),
        'Uranus': ephem.Uranus(data_day),
        'Neptune': ephem.Neptune(data_day),
    }

    if planet not in planets_dict.keys():
        update.message.reply_text('Такой планеты рядом нет')
    else:
        constellation = ephem.constellation(planets_dict[planet])[1]
        update.message.reply_text(f'Планета: {planet} \nCегодня в созвездии {constellation}')


def main():
    mybot = Updater(tele_token, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", planet_constellation))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
