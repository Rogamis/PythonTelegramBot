import telebot
import Config 

from telebot import types

bot = telebot.TeleBot(Config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
		sti = open('qq.webp', 'rb')
		bot.send_sticker(message.chat.id, sti)

	# keyboard
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton("Полезные ссылки 💻")
		item2 = types.KeyboardButton("Какие команды есть")
	
		markup.add(item1, item2)


		bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, за информацией обращайся ниже".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'Полезные ссылки 💻':
			bot.send_message(message.chat.id, 'Instargam: www.instagram.com/krivbasslions/?hl=ru')
			bot.send_message(message.chat.id, '"Telegram: t.me/krivbasslions"')
		elif message.text == 'Какие команды есть':

			bot.send_message(message.chat.id, '🎮 CS GO: HellPeek, ATLANTA, CarpeDiem, GSAG, CyberTiger')
			bot.send_message(message.chat.id, '🎮 Dota: MainBrand')
# RUN
bot.polling(none_stop=True)

