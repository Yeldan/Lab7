import telegram
bot = telegram.Bot(token = '313895624:AAHCgMSrk1y2xr5i7X6h-NBsC32b1HwBT_A')
from telegram.ext import Updater
updater = Updater(token = '313895624:AAHCgMSrk1y2xr5i7X6h-NBsC32b1HwBT_A')
dispatcher = updater.dispatcher

def say_kettik(bot, update):
	bot.sendMessage(chat_id = update.message.chat_id, text = "kettik, wws")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', say_kettik)
dispatcher.add_handler(start_handler)

def weather(bot, update):
	import requests
	from bs4 import BeautifulSoup
	url = 'http://kazhydromet.kz/ru/almaty'
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	wtext = soup.select(".w_map span")[0].text
	bot.sendMessage(chat_id = update.message.chat_id, text = wtext)

from telegram.ext import CommandHandler
weather_handler = CommandHandler('weather', weather)
dispatcher.add_handler(weather_handler)


def petrol(bot, update):
	import requests
	from bs4 import BeautifulSoup
	url = "http://helios.kz/toplivo/tseny-na-benzin/"
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	li = soup.select("#petroil-prices li")[0]
	name = li.select("span.name")[0].text
	rate = float(li.select("span.value")[0].text.replace(",", "."))
	wtext = name + " " + str(rate)
	bot.sendMessage(chat_id = update.message.chat_id, text = wtext)

from telegram.ext import CommandHandler
petrol_handler = CommandHandler('petrol', petrol)
dispatcher.add_handler(petrol_handler)

def currency(bot, update):
	import requests
	from bs4 import BeautifulSoup
	url = "http://www.nationalbank.kz/?furl=cursFull&switch=rus"
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	tr = soup.select("table.gen4 tr")[10]
	name = tr.select("td.gen7")[0].text
	rate = float(tr.select("td.gen7")[2].text.replace(",", "."))
	wtext = name + " " + str(rate)
	bot.sendMessage(chat_id = update.message.chat_id, text = wtext)

from telegram.ext import CommandHandler
currency_handler = CommandHandler('currency', currency)
dispatcher.add_handler(currency_handler)


updater.start_polling()	

