# import telebot
# import config


# # Установить токен вашего телеграм-бота
# bot = telebot.TeleBot(config.TOKEN)



# # Обработчик команды /start
# @bot.message_handler(commands=['start'])
# def start(message):
#       user = message.from_user
#       welcome_message = (
#       "   🍻 Приветствуем вас в *Paulaner Brauhaus Almaty*! 🍻\n\n"
#       f"Привет, {user.first_name}!\n\n"
#       "   🌟 Откройте для себя аутентичное пиво и вкуснейшие блюда.\n"
#       "   🍽️ Выбирайте из нашего разнообразного меню и погружайтесь в культуру!\n"
#       "   🎉 Присоединяйтесь к нам на мероприятиях и дегустациях.\n"
#       "   📅 Не упустите новости и эксклюзивные предложения.\n\n"
#       "   Поднимем бокалы за незабываемые моменты в *Paulaner Brauhaus*!\n\n"
#       "🍺 Давайте создадим пивные истории вместе! 🍺"
#   )
     
    
#   # Создание клавиатуры с кнопкой меню
#       history_button = telebot.types.InlineKeyboardButton("📜 История", url="https://telegra.ph/Istorii-pivovarni-Paulaner-08-15")

#       brewing_art_button = telebot.types.InlineKeyboardButton("🍻 Мюнхенское искусство пивоварения", url="https://telegra.ph/Kak-delayut-pivo-Paulaner-08-15")
#       menu_button = telebot.types.InlineKeyboardButton("📖 Меню", url="https://touch2phone.kz/paulaner#rec535966332")
#       schedule_button = telebot.types.InlineKeyboardButton("🕒 График работы", callback_data="schedule")
#       address_button = telebot.types.InlineKeyboardButton("📍 Наш адрес", url="https://go.2gis.com/s6j68q")
#       call_button = telebot.types.InlineKeyboardButton("📞 Заказать столик", callback_data="call")
#       news_button = telebot.types.InlineKeyboardButton("🗒️ Спецпредложения", url="https://telegra.ph/Novinki-08-15-3")
#       keyboard =telebot.types.InlineKeyboardMarkup().add(history_button).add(brewing_art_button).add(menu_button).add(schedule_button).add(address_button).add(news_button)
        
#      # Отправка сообщения с внутренней клавиатурой
#       bot.send_message(chat_id=message.chat.id, text=welcome_message, reply_markup=keyboard, parse_mode='MARKDOWN')


# # Обработчик нажатия на кнопку "Меню"
# @bot.callback_query_handler(func=lambda call: call.data.startswith('menu'))
# def handle_menu_button(callback_query):
#     bot.answer_callback_query(callback_query.id)
#     bot.send_message(callback_query.message.chat.id, "Вы перешли на наш веб-сайт с меню: https://touch2phone.kz/paulaner#rec535966332")
    
    
# # Обработчик нажатия на кнопку "График работы"
# @bot.callback_query_handler(func=lambda call: call.data == 'schedule')
# def handle_schedule_button(callback_query):
#     schedule_info = (
#         "🕒 График работы *Paulaner Brauhaus Almaty*:\n"
#         "    Вс - Чт: 12:00 - 01:00\n"
#         "    Пт - Сб: 12:00 - 02:00\n"
#         "Добро пожаловать на посещение в удобное для вас время!"
#     )

#     bot.answer_callback_query(callback_query.id)
#     bot.send_message(callback_query.message.chat.id, schedule_info, parse_mode='MARKDOWN')    


# @bot.callback_query_handler(func=lambda call: call.data == 'call')
# def handle_call_button(callback_query):
#     call_info = (
#         "📞 Для заказа столика или других вопросов, пожалуйста, позвоните по номерам:\n"
#         "  +77056255111 (менеджер по резервированию столов)\n"
#         "  +77711544999 (общие вопросы и консультации)"
#     )

#     bot.answer_callback_query(callback_query.id)
#     bot.send_message(callback_query.message.chat.id, call_info, parse_mode='MARKDOWN')







bot.polling()

