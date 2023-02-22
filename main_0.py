import bank_api_0
import telebot
import logging
import types
import telebot_token
from datetime import date
from datetime import timedelta
from telebot import types
bot = telebot.TeleBot(
    telebot_token.token, parse_mode=None)
telebot.logger.setLevel(logging.DEBUG)
logger = telebot.logger

exchange_rates = bank_api_0.them_rates()


@bot.message_handler()
def start(message):
    if message.text == '/start':
        keyboard = types.InlineKeyboardMarkup()
        key_ru = types.InlineKeyboardButton(text='RU', callback_data='ru')
        key_en = types.InlineKeyboardButton(text='EN', callback_data='en')
        keyboard.add(key_ru)
        keyboard.add(key_en)
        bot.send_message(message.from_user.id,
                         "Please, choose your language.", reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, "please type /start")


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "en":
        keyboard = types.InlineKeyboardMarkup()
        key_en_books = types.InlineKeyboardButton(
            text="Books", callback_data='en-books')
        key_en_rates = types.InlineKeyboardButton(
            text="Rates", callback_data='en-rates')
        keyboard.add(key_en_books)
        keyboard.add(key_en_rates)
        bot.send_message(
            call.message.chat.id, "Now let's choose between some books reviews and the current exchange rates. Make your choice.", reply_markup=keyboard)
    elif call.data == 'ru':
        keyboard = types.InlineKeyboardMarkup()
        key_ru_books = types.InlineKeyboardButton(
            text="Книги", callback_data='ru-books')
        key_ru_rates = types.InlineKeyboardButton(
            text="Курсы", callback_data='ru-rates')
        keyboard.add(key_ru_books)
        keyboard.add(key_ru_rates)
        bot.send_message(
            call.message.chat.id, "Теперь давай выберем между обзором на некоторые серии книг и текущим курсом валют. Выбирай.", reply_markup=keyboard)
# en books
    elif call.data == "en-books":
        keyboard = types.InlineKeyboardMarkup()
        key_sci_fi = types.InlineKeyboardButton(
            text="Sci-Fi", callback_data='sci-fi')
        key_fantasy = types.InlineKeyboardButton(
            text="Fantasy", callback_data='fantasy')
        keyboard.add(key_fantasy)
        keyboard.add(key_sci_fi)
        bot.send_message(
            call.message.chat.id, "Now let's choose the genre. Make your choice.", reply_markup=keyboard)
    elif call.data == "sci-fi":
        keyboard = types.InlineKeyboardMarkup()
        key_sci_fi_1 = types.InlineKeyboardButton(
            text="Астровитянка", callback_data='sci-fi-1')
        keyboard.add(key_sci_fi_1)
        bot.send_message(
            call.message.chat.id, "Sci-fi it is then. Let's see what there is to see:", reply_markup=keyboard)
    elif call.data == "fantasy":
        keyboard = types.InlineKeyboardMarkup()
        key_fantasy_1 = types.InlineKeyboardButton(
            text="Harry Potter", callback_data='fantasy-1')
        keyboard.add(key_fantasy_1)
        key_fantasy_2 = types.InlineKeyboardButton(
            text="the Lord of the Rings", callback_data='fantasy-2', reply_markup=keyboard)
        keyboard.add(key_fantasy_2)
        bot.send_message(
            call.message.chat.id, "Alright then, let me show what I have here:", reply_markup=keyboard)
    elif call.data == 'sci-fi-1':
        bot.send_message(call.message.chat.id, "Now I'm going to quote rerankar's opinion on this one: 'The only sci-fi story that I'm going to think as of a true masterpiece. Starting with the name itself - despite my English CEFR level is C1 I lack vacabulary to translate the name of the series: it's sort of a pun made of Russian words 'остров' (island) and 'астронавт' (astonaut)'. The book series contain quite a good lovestory in the future - approximately a century or two since nowadays, but the setting itself is marvelous for me as it never breaks the law of physics. Nuff said.'")
    elif call.data == 'fantasy-1':
        bot.send_message(call.message.chat.id,
                         "Harry Potter is a modern classic created by mistress Rowling about a boy aged of eleven to seventeen years old who studies at the only British school of sorcery, has fun, celebrates Christmas and tries to survive the war between so-called 'good mages' and hordes of a version of biblical king Herod I the Great.")
    elif call.data == 'fantasy-2':
        bot.send_message(call.message.chat.id, "To be honest, rerankar knows no human who wouldn't know of the epic story of Frodo Baggins and the world which became the fundament of innumerous fantasy and even sci-fi worlds, e.g. some parts of Harry Potter world or several (hundreds?) worlds of the Warhammer 40 000 universe. I'm afraid rerankar is in fear of telling anything about - the risk of spoilers terrorize his mind.")
# ru books
    elif call.data == "ru-books":
        keyboard = types.InlineKeyboardMarkup()
        key_sci_fi_ru = types.InlineKeyboardButton(
            text="Научная фантастика", callback_data='sci-fi-ru')
        key_fantasy_ru = types.InlineKeyboardButton(
            text="Фэнтези", callback_data='fantasy-ru')
        keyboard.add(key_fantasy_ru)
        keyboard.add(key_sci_fi_ru)
        bot.send_message(
            call.message.chat.id, "С языком определились, а теперь следует выбрать жанр.", reply_markup=keyboard)
    elif call.data == "sci-fi-ru":
        keyboard = types.InlineKeyboardMarkup()
        key_sci_fi_1_ru = types.InlineKeyboardButton(
            text="Астровитянка", callback_data='sci-fi-1')
        keyboard.add(key_sci_fi_1_ru)
        bot.send_message(
            call.message.chat.id, "Научная фантастика? Понял-принял, вот, что у меня есть:", reply_markup=keyboard)
    elif call.data == "fantasy-ru":
        keyboard = types.InlineKeyboardMarkup()
        key_fantasy_1_ru = types.InlineKeyboardButton(
            text="Гарри Поттер", callback_data='fantasy-1-ru')
        keyboard.add(key_fantasy_1_ru)
        key_fantasy_2_ru = types.InlineKeyboardButton(
            text="Властелин колец", callback_data='fantasy-2-ru', reply_markup=keyboard)
        keyboard.add(key_fantasy_2_ru)
        bot.send_message(
            call.message.chat.id, "Итак, жанр фэнтэзи. Прошу взглянуть на то, о чём мне ведомо.", reply_markup=keyboard)
    elif call.data == 'sci-fi-1-ru':
        bot.send_message(call.message.chat.id, "Само слово 'астровитянка' - игра слов от 'астронавт' и 'островитянка', которая описывает суть главной героини: она почти всё детство прожила на астероиде. Трилогия содержит отличную ветку подростковой любви, достаточно неплохой боевой сюжет, но что больше прочего зацепило моё внимание - это проработка мира: автор пользовался только теми научными данными, что были ему доступны и известны в момент написания книг, без выкрутасов вроде гипердвигателя, а также, если какие-то теории получали доказательства несостоятельности, то он их аккуратно вырезал из повествования в следующей книге. За такой подход данная трилогия и получила моё искреннее уважение и почтение. Рекомендую её изо всех сил.")
    elif call.data == 'fantasy-1-ru':
        bot.send_message(call.message.chat.id,
                         "Серия 'Гарри Поттер' или, как её ещё называют, 'поттериана' - серия из семи книг от Джоан Роулинг, описывающая семь лет жизни нескольких юнцов, пытающихся наслаждаться жизнью, учиться магии в единственной в Великобритании подобной школе и противостоять местному аналогу библейского Ирода I Великого. Эти книги стали современной классикой, но у этой серии есть проблема: смотреть (да, все книги экранизированы) или читать её следует максимум пару-тройку раз, иначе начинаешь подмечать всё больше сюжетных дыр и пробелов в лоре и механике этой вселенной. Однако на пару раз это точно будет красивая история о юных магах.")
    elif call.data == 'fantasy-2-ru':
        bot.send_message(call.message.chat.id, "Если честно, я даже не знаю, есть ли смысл говорить что-то об этой группе книг - о самой трилогии 'Властелин колец', о сказке 'Хоббит' и об энциклопедии 'Сильмариллион', потому как мало кто не знает хотя бы о трилогии. Я считаю достаточным сказать, что мир сэра Толкиена создал основу для множества иных миров, причём не только фэнтэзи, но и в жанре научной фантастики местами. Остальное узнаете сами из трудов профессора. Ну, или хотя бы из экранизаций П. Джексона, что были выпущены в первой половине нулевых, - это, вероятно, меньше времени займёт.")
# en rates
    elif call.data == "en-rates":
        bot.send_message(call.message.chat.id, "Yesterday's (or Friday's, if today is Monday) exchange rates are " +
                         str(round(exchange_rates, 4)) + ' USD per 1 EUR and ' + str(round((1/exchange_rates), 4)) + ' EUR per 1 USD. Type /start to return.')
# ru rates
    elif call.data == "ru-rates":
        bot.send_message(call.message.chat.id, 'Вчерашний (или пятничный, если сегодня понедельник) курс валют: '+str(
            round(exchange_rates, 4))+' USD за 1 EUR и '+str(round((1/exchange_rates), 4))+' EUR за 1 USD. Напишите /start для возвращения к началу.')


bot.infinity_polling()
