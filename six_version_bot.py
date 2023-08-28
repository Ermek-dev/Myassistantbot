# Вам нужно импортировать необходимые библиотеки
from telebot import types
import telebot


TOKEN = '6622103483:AAHXL3PO7gQDYjJJd9OtUHZoeZ-FYXzDkRc'

bot = telebot.TeleBot(TOKEN)

# Создайте переменную для хранения состояния пользователя
user_states = {}
user_password_attempts = {}

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

    markup.add(item1, item2, item3, item4, item5, item6)

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

    bot.send_message(chat_id=message.chat.id, text=welcome_message,
                     reply_markup=markup, parse_mode='MARKDOWN')


# Добавьте обработчик для кнопки "🗒️ Для сотрудников"
@bot.message_handler(func=lambda message: message.text == '🗒️ Для сотрудников')
def ask_for_password(message):
    user_states[message.chat.id] = 'waiting_password'
    user_password_attempts[message.chat.id] = 0  # Устанавливаем начальное количество попыток
    bot.send_message(message.chat.id, "Введите пароль:")


 #Добавьте обработчик для кнопки "🗒️ Для сотрудников"
@bot.message_handler(func=lambda message: message.text == '🗒️ Для сотрудников')
def ask_for_password(message):
    user_states[message.chat.id] = 'waiting_password'
    user_password_attempts[message.chat.id] = 0  # Устанавливаем начальное количество попыток
    bot.send_message(message.chat.id, "Введите пароль:")

# Добавьте обработчик для ввода пароля
@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'waiting_password')
def handle_password(message):
    if message.text == '1111':  # Замените на реальный пароль
        user_states[message.chat.id] = 'authenticated'
        user_password_attempts[message.chat.id] = 0  # Сбрасываем счетчик попыток
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('🔄 Ротации')
        item2 = types.KeyboardButton('📜 История пивоварни')
        item3 = types.KeyboardButton('🍻 Процесс пивоварения')
        item4 = types.KeyboardButton('🍺 Виды пива')
        item5 = types.KeyboardButton('📚 Файлы')
        item6 = types.KeyboardButton('🍽 Сервис')
        about_us_button = types.KeyboardButton('📝 О нас')
        back = types.KeyboardButton('⬅️ Назад')
        markup.add(item1, item2, item3, item4, item5, item6, about_us_button, back)
        
        bot.send_message(message.chat.id, "Пароль верный. Вы перешли в раздел '🗒️ Для сотрудников'", reply_markup=markup)
    else:
        user_password_attempts[message.chat.id] += 1  # Увеличиваем счетчик попыток
        remaining_attempts = 3 - user_password_attempts[message.chat.id]
        if remaining_attempts > 0:
            bot.send_message(message.chat.id, f"Неверный пароль. Попробуйте снова. Осталось попыток: {remaining_attempts}")
        else:
            bot.send_message(message.chat.id, "Превышено количество попыток. Попробуйте позже.")
            user_states[message.chat.id] = None
            user_password_attempts[message.chat.id] = 0
            
@bot.message_handler(func=lambda message: message.text == '👨‍🍳 Шеф-повар' and user_states.get(message.chat.id) == 'authenticated')
def show_chef_info(message):
    chef_info = (
        "Наш шеф-повар Павел – настоящий маг в кухне! Он создает уникальные блюда, сочетая традиции и новаторство. "
        "Благодаря его усилиям, наше меню всегда остается интересным и вдохновляющим. "
        "Шеф-повар гарантирует высокое качество и неповторимый вкус каждого блюда!"
    )
    bot.send_message(message.chat.id, chef_info)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == "📖 Меню":
            menu_button = types.InlineKeyboardButton(
                "📖 Меню", url="https://touch2phone.kz/paulaner#rec535966332")
            menu_markup = types.InlineKeyboardMarkup().add(menu_button)
            bot.send_message(
                message.chat.id, "Вы переходит на сайт", reply_markup=menu_markup)

        elif message.text == '🎉 Афиша':
            afisha_button = types.InlineKeyboardButton(
                '🎉 Афиша', url="https://sxodim.com/almaty/place/paulaner-braeuhaus-almaty")
            afisha_markup = types.InlineKeyboardMarkup().add(afisha_button)
            bot.send_message(
                message.chat.id, "Вы переходит на сайт", reply_markup=afisha_markup)

        elif message.text == '🍽️ Уникальное предложение':
            special_offer_button = types.InlineKeyboardButton(
                '🍽️ Уникальное предложение', url="https://telegra.ph/Novinki-08-15-3")
            special_offer_markup = types.InlineKeyboardMarkup().add(special_offer_button)
            bot.send_message(message.chat.id, "Вы переходит на сайт",
                             reply_markup=special_offer_markup)

        elif message.text == "📞 Связаться с нами":
            phone_markup = types.ReplyKeyboardMarkup(
                row_width=1, resize_keyboard=True)
            item1 = types.KeyboardButton('☎️ +77056255111')
            item2 = types.KeyboardButton('☎️ +77711544999')
            back = types.KeyboardButton('⬅️ Назад')
            phone_markup.add(item1, item2, back)
            bot.send_message(
                message.chat.id, text="Выберите номер телефона:", reply_markup=phone_markup)

        elif message.text == '📍 Наш адрес':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🗺 Google Карты')
            item2 = types.KeyboardButton('🌍 Яндекс.Карты')
            item3 = types.KeyboardButton('🗺 2GIS')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(item1, item2, item3, back)
            bot.send_message(
                message.chat.id, text="Выберите карту для просмотра адреса:", reply_markup=markup)

        elif message.text == "🌍 Яндекс.Карты":
            bot.send_message(
                message.chat.id, text="Ссылка на адрес в Яндекс.Картах: https://yandex.ru/maps/org/paulaner_brauhaus/50803496758/?ll=76.915955%2C43.247914&z=17")

        elif message.text == "🗺 2GIS":
            bot.send_message(
                message.chat.id, text="Ссылка на адрес в 2GIS: https://2gis.kz/almaty/firm/70000001055876564")

        elif message.text == "🗺 Google Карты":
            bot.send_message(message.chat.id, text="Ссылка на адрес в Google Картах: https://www.google.com/maps/place/Paulaner+Br%C3%A4uhaus+Almaty/@43.2478844,76.9133374,17z/data=!3m1!4b1!4m6!3m5!1s0x3883698bec7f81b1:0x162127256edeaf21!8m2!3d43.2478844!4d76.9159123!16s%2Fg%2F11pq98ncw8?entry=ttu")

        elif message.text == '🗒️ Для сотрудников':
            if user_states.get(message.chat.id) == 'authenticated':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('🔄 Ротации')
                item2 = types.KeyboardButton('📜 История пивоварни')
                item3 = types.KeyboardButton('🍻 Процесс пивоварения')
                item4 = types.KeyboardButton('🍺 Виды пива')
                item5 = types.KeyboardButton('📚 Файлы')
                item6 = types.KeyboardButton('🍽  Сервис')
                chef_info_button = types.KeyboardButton('👨‍🍳 Шеф-повар')
                back = types.KeyboardButton('⬅️ Назад')
                markup.add(item1, item2, item3, item4, item5,
                           item6, chef_info_button, back)

                bot.send_message(
                    message.chat.id, "Вы перешли в раздел '🗒️ Для сотрудников' ", reply_markup=markup)
            else:
                user_states[message.chat.id] = 'waiting_password'
                bot.send_message(message.chat.id, "Введите пароль:")

        elif message.text == '⬅️ Назад':
            markup = types.ReplyKeyboardMarkup()
            item1 = types.KeyboardButton('📖 Меню')
            item2 = types.KeyboardButton('🎉 Афиша')
            item3 = types.KeyboardButton('🍽️ Уникальное предложение')
            item4 = types.KeyboardButton('📞 Связаться с нами')
            item5 = types.KeyboardButton('📍 Наш адрес')
            item6 = types.KeyboardButton('🗒️ Для сотрудников')

            markup.add(item1, item2, item3, item4, item5, item6)
            bot.send_message(message.chat.id, 'Назад', reply_markup=markup)

        elif message.text == "🔄 Ротации":
            rotations_button = types.InlineKeyboardButton(
                "Ротации", url="https://drive.google.com/drive/folders/15CZZSpUtDHEn1KN5D75Q0Qx7Oer-KUHM?usp=sharing")
            rotations_markup = types.InlineKeyboardMarkup().add(rotations_button)
            bot.send_message(
                message.chat.id, "Вы переходите к ротациям", reply_markup=rotations_markup)

        elif message.text == "📜 История пивоварни":
            history_message = "Здесь вы можете узнать интересные факты о нашей пивоварне и ее истории."
            history_button = types.InlineKeyboardButton(
                "Перейти:", url="https://telegra.ph/Istorii-pivovarni-Paulaner-08-15")
            history_markup = types.InlineKeyboardMarkup().add(history_button)

            bot.send_message(message.chat.id, text=history_message,
                             reply_markup=history_markup)

        elif message.text == "🍻 Процесс пивоварения":
            brewing_process_message = "Расскажем вам о процессе создания нашего вкусного пива!"
            brewing_process_button = types.InlineKeyboardButton(
                "Перейти:", url="https://telegra.ph/Process-pivovareniya-08-16")
            brewing_process_markup = types.InlineKeyboardMarkup().add(brewing_process_button)

            bot.send_message(message.chat.id, text=brewing_process_message,
                             reply_markup=brewing_process_markup)

        elif message.text == "🍺 Виды пива":
            beer_types_message = "У нас есть широкий выбор различных сортов пива. Попробуйте и выберите свой любимый!"
            beer_types_button = types.InlineKeyboardButton(
                "Перейти:", url="https://telegra.ph/Kak-varyat-pivovidyinteresnye-fakty-08-16")
            beer_types_markup = types.InlineKeyboardMarkup().add(beer_types_button)

            bot.send_message(
                message.chat.id, text=beer_types_message, reply_markup=beer_types_markup)

        elif message.text == "📚 Файлы":
            file_url = 'https://drive.google.com/drive/folders/1WhRMuz6OmkN0PiLm8SF1N03tXgkL4eeF?usp=drive_link'
            files_types_message = "Здесь вы найдете полезные файлы и документы."
            files_types_button = types.InlineKeyboardButton(
                "Перейти:", url=file_url)
            files_types_markup = types.InlineKeyboardMarkup().add(files_types_button)

            bot.send_message(
                message.chat.id, text=files_types_message, reply_markup=files_types_markup)

        elif message.text == "🍽 Сервис":
            service_types_message = "7 шагов сервиса: обслуживание посетителей в ресторане, основные стандарты качества"
            service_types_button = types.InlineKeyboardButton(
                "Перейти:", url="https://telegra.ph/Standarty-restorannogo-servisa-08-28")
            service_types_markup = types.InlineKeyboardMarkup().add(service_types_button)

            bot.send_message(
                message.chat.id, text=service_types_message, reply_markup=service_types_markup)


bot.polling(none_stop=True)            