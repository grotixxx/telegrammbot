from settings import bot, requests, b, \
    random, types, telebot



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    joke = types.KeyboardButton('Анекдот')
    markup.add(joke)
    bot.send_message(message.chat.id, 'Нажми на кнопку', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Анекдот"):
        bot.send_message(message.chat.id, text=list_of_anekdots[0])
        del list_of_anekdots[0]


URL = 'https://anekdot-ua.net/'
def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='joke-body')
    return [c.text for c in anekdots]
list_of_anekdots = parser(URL)
random.shuffle(list_of_anekdots)

bot.infinity_polling()
