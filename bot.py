import telebot
import os
import config


# Установить токен вашего телеграм-бота
bot = telebot.TeleBot(config.TOKEN)



# Обработчик команды /start
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('/home/severus/myprojects/paulanerassistantbot/static/images/stick.webp','rb')
    bot.send_sticker(message.chat.id,sti)
    bot.send_message(message.chat.id, "Welcome,{0.first_name}!\nЯ-<b>{1.first_name}</b>,бот созданный чтобы быть твоим другом.".format(message.from_user,bot.get_me()),parse_mode='html')


# Запуск бота
bot.polling()

