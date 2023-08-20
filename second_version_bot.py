import telebot
from telebot import types
import config


# Установить токен вашего телеграм-бота
bot = telebot.TeleBot(config.TOKEN)

# Словарь для хранения состояний пользователей
user_states = {}



@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user
    markup = types.ReplyKeyboardMarkup()
    item1 = types.KeyboardButton('📖 Меню')
    item2 = types.KeyboardButton('🎉 Афиша')
    item3 = types.KeyboardButton('🍽️ Уникальное предложение')
    item4 = types.KeyboardButton('📞 Связаться с нами')
    item5 = types.KeyboardButton('📍 Наш адрес')
    item6 = types.KeyboardButton('🗒️ Для сотрудников')
    
    
    markup.add(item1,item2,item3,item4,item5,item6)
    
    welcome_message = (
      "   🍻 Приветствуем вас в *Paulaner Brauhaus Almaty*! 🍻\n\n"
      f"Привет, {user.first_name}!\n\n"
      "   🌟 Откройте для себя аутентичное пиво и вкуснейшие блюда.\n"
      "   🍽️ Выбирайте из нашего разнообразного меню и погружайтесь в культуру!\n"
      "   🎉 Присоединяйтесь к нам на мероприятиях и дегустациях.\n"
      "   📅 Не упустите новости и эксклюзивные предложения.\n\n"
      "   Поднимем бокалы за незабываемые моменты в *Paulaner Brauhaus*!\n\n"
      "🍺 Давайте создадим пивные истории вместе! 🍺"
  )
    
    bot.send_message(chat_id=message.chat.id, text=welcome_message, reply_markup=markup, parse_mode='MARKDOWN')
   
    
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':             
        if message.text == "📖 Меню":
            menu_button = types.InlineKeyboardButton("📖 Меню", url="https://touch2phone.kz/paulaner#rec535966332")
            menu_markup = types.InlineKeyboardMarkup().add(menu_button)
            bot.send_message(message.chat.id,"Вы переходит на сайт",reply_markup=menu_markup)
            
        elif message.text == '🎉 Афиша':
            afisha_button = types.InlineKeyboardButton('🎉 Афиша', url="https://sxodim.com/almaty/place/paulaner-braeuhaus-almaty")
            afisha_markup = types.InlineKeyboardMarkup().add(afisha_button)
            bot.send_message(message.chat.id,"Вы переходит на сайт",reply_markup=afisha_markup)  
        
        elif message.text == '🍽️ Уникальное предложение':
            special_offer_button = types.InlineKeyboardButton('🍽️ Уникальное предложение', url="https://telegra.ph/Novinki-08-15-3")
            special_offer_markup = types.InlineKeyboardMarkup().add(special_offer_button)
            bot.send_message(message.chat.id,"Вы переходит на сайт",reply_markup=special_offer_markup)      
            
        elif message.text == "📞 Связаться с нами":
            phone_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            item1 = types.KeyboardButton('☎️ +77056255111')
            item2 = types.KeyboardButton('☎️ +77711544999')
            back = types.KeyboardButton('⬅️ Назад')
            phone_markup.add(item1, item2, back)
            bot.send_message(message.chat.id, text="Выберите номер телефона:", reply_markup=phone_markup)

        elif message.text == '📍 Наш адрес':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🗺 Google Карты')
            item2 = types.KeyboardButton('🌍 Яндекс.Карты')
            item3 = types.KeyboardButton('🗺 2GIS')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(item1, item2,item3, back) 
            bot.send_message(message.chat.id, text="Выберите карту для просмотра адреса:", reply_markup=markup)
        
        elif message.text == "🌍 Яндекс.Карты":
            bot.send_message(message.chat.id, text="Ссылка на адрес в Яндекс.Картах: https://yandex.ru/maps/org/paulaner_brauhaus/50803496758/?ll=76.915955%2C43.247914&z=17")  
                 
        elif message.text == "🗺 2GIS":
            bot.send_message(message.chat.id, text="Ссылка на адрес в 2GIS: https://2gis.kz/almaty/firm/70000001055876564")
            
        elif message.text == "🗺 Google Карты":
            bot.send_message(message.chat.id, text="Ссылка на адрес в Google Картах: https://www.google.com/maps/place/Paulaner+Br%C3%A4uhaus+Almaty/@43.2478844,76.9133374,17z/data=!3m1!4b1!4m6!3m5!1s0x3883698bec7f81b1:0x162127256edeaf21!8m2!3d43.2478844!4d76.9159123!16s%2Fg%2F11pq98ncw8?entry=ttu")
        
        elif message.text == '🗒️ Для сотрудников':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🔄 Ротации')
            item2 = types.KeyboardButton('📜 История пивоварни')
            item3 = types.KeyboardButton('🔧 Процесс пивоварения')
            item4 = types.KeyboardButton('🍺 Виды пива')
            item5 = types.KeyboardButton('📚 Файлы')
            item6 = types.KeyboardButton('🔧 Сервис')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(item1,item2,item3,item4,item5,item6,back)
            
            bot.send_message(message.chat.id,"Вы перешли в раздел '🗒️ Для сотрудников' ",reply_markup=markup)

            
        elif message.text == '⬅️ Назад':
            markup = types.ReplyKeyboardMarkup()
            item1 = types.KeyboardButton('📖 Меню')
            item2 = types.KeyboardButton('🎉 Афиша')
            item3 = types.KeyboardButton('🍽️ Уникальное предложение')
            item4 = types.KeyboardButton('📞 Связаться с нами')
            item5 = types.KeyboardButton('📍 Наш адрес')
            item6 = types.KeyboardButton('🗒️ Для сотрудников')
        
        
            markup.add(item1,item2,item3,item4,item5,item6)
            bot.send_message(message.chat.id,'Назад',reply_markup = markup)
            
        elif message.text == "🔄 Ротации":
            rotations_button = types.InlineKeyboardButton("Ротации",url="https://drive.google.com/drive/folders/15CZZSpUtDHEn1KN5D75Q0Qx7Oer-KUHM?usp=sharing")
            rotations_markup = types.InlineKeyboardMarkup().add(rotations_button)
            bot.send_message(message.chat.id,"Вы переходите к ротациям",reply_markup=rotations_markup)
            
        elif message.text == "📜 История пивоварни":
            history_message = "Здесь вы можете узнать интересные факты о нашей пивоварне и ее истории."
            history_button = types.InlineKeyboardButton("Перейти:", url="https://telegra.ph/Istorii-pivovarni-Paulaner-08-15")
            history_markup = types.InlineKeyboardMarkup().add(history_button)
            
            bot.send_message(message.chat.id, text=history_message, reply_markup=history_markup)
            
        elif message.text == "🔧 Процесс пивоварения":
            brewing_process_message = "Расскажем вам о процессе создания нашего вкусного пива!"
            brewing_process_button = types.InlineKeyboardButton("Перейти:", url="https://telegra.ph/Process-pivovareniya-08-16")
            brewing_process_markup = types.InlineKeyboardMarkup().add(brewing_process_button)
            
            bot.send_message(message.chat.id, text=brewing_process_message, reply_markup=brewing_process_markup)
            
        elif message.text == "🍺 Виды пива":
            beer_types_message = "У нас есть широкий выбор различных сортов пива. Попробуйте и выберите свой любимый!"
            beer_types_button = types.InlineKeyboardButton("Перейти:", url="https://telegra.ph/Kak-varyat-pivovidyinteresnye-fakty-08-16")
            beer_types_markup = types.InlineKeyboardMarkup().add(beer_types_button)
            
            bot.send_message(message.chat.id, text=beer_types_message, reply_markup=beer_types_markup)
            
        elif message.text == "📚 Файлы":
            file_url = 'https://drive.google.com/drive/folders/1WhRMuz6OmkN0PiLm8SF1N03tXgkL4eeF?usp=drive_link'
            files_types_message = "Здесь вы найдете полезные файлы и документы."
            files_types_button = types.InlineKeyboardButton("Перейти:", url=file_url)
            files_types_markup = types.InlineKeyboardMarkup().add(files_types_button)
            
            bot.send_message(message.chat.id, text=files_types_message, reply_markup=files_types_markup)
              
            

    
            
bot.polling(none_stop = True)    
        
        
        
        
 
