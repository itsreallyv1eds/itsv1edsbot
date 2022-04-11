import telebot
import random
from telebot import types
f = open('data/holiday.txt', 'r', encoding='UTF-8')
holiday = f.read().split('\n')
f.close()
f = open('data/sobitiya.txt', 'r', encoding='UTF-8')
sobitiya  = f.read().split('\n')
f.close()
bot = telebot.TeleBot('ваш токен')
@bot.message_handler(commands=["start"])
def start(m, res=False):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Праздники")
        item2=types.KeyboardButton("События")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Нажми: \nПраздники - чтобы узнать какие сегодня праздники\nСобытия - чтобы узнать какие сегодня события ',  reply_markup=markup)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Праздники' :
            answer = random.choice(holiday)
    elif message.text.strip() == 'События':
            answer = random.choice(sobitiya)
    bot.send_message(message.chat.id, answer)
bot.polling(none_stop=True, interval=0)