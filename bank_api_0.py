import requests
import telebot
from datetime import date
from datetime import timedelta
bot = telebot.TeleBot('5819407124:AAH_e6dPrSS33Wa7lwQLCSvqRSyqkPw3Vfo')


def them_rates():
    if date.today().weekday() == 0:
        exchange_rates = requests.get('https://sdw-wsrest.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?includeHistory=false&startPeriod=' + str(
            date.today() - timedelta(days=3)) + '&format=jsondata').json()['dataSets'][0]['series']['0:0:0:0:0']['observations']['0'][0]
    else:
        exchange_rates = requests.get('https://sdw-wsrest.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?includeHistory=false&startPeriod=' + str(
            date.today() - timedelta(days=1)) + '&format=jsondata').json()['dataSets'][0]['series']['0:0:0:0:0']['observations']['0'][0]
    return exchange_rates
