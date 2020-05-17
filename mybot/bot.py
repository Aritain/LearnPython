import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

# Объявляем конфиг бота
logging.basicConfig(filename='bot.log', level=logging.INFO)

# Функция-обработчик команды /start
def greet_user(update, context):
	update.message.reply_text('Привет!')
	#print(update.message.chat.username)
	
# Функция-обработчик текстовых сообщений	
def talk_to_me(update, context):
	update.message.reply_text(update.message.text)

def main():
	# Объявляем бота с полученным токеном
	mybot = Updater(settings.API_KEY, use_context = True)
	
	# Объявление диспетчера и описание хендлеров
	dp = mybot.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))
	
	# Запускаем апдейтер и пишем это в лог
	logging.info("Bot started")
	mybot.start_polling()
	mybot.idle()
	
if __name__ == "__main__":	
	main()