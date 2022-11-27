'''Створіть програму для отримання курсу валют за певний період.
- отримати від користувача дату (це може бути як один день так і інтервал - початкова і кінцева дати, 
продумайте механізм реалізації) і назву валюти
- вивести курс по відношенню до гривні на момент вказаної дати (або за кожен день у вказаному інтервалі)
- не забудьте перевірку на валідність введених даних'''

from urllib.parse import urljoin
import requests
import json
from datetime import timedelta, date, datetime


class ExchangeRateParser:
	BASE_URL = 'https://api.privatbank.ua/'
	IN_BANK_RATE_URL = urljoin(BASE_URL, 'p24api/exchange_rates')


	def get_exchange_rate(self, start_date, end_date, currency):
		day_count = (end_date - start_date).days + 1
		print(f" Дата        Валюта      Купівля    Продаж ")
		for single_date in [d for d in (start_date + timedelta(n) for n in range(day_count)) if d <= end_date]:
			date_number = single_date.strftime('%d.%m.%Y')
			exchange_rate_page = requests.get(self.IN_BANK_RATE_URL, {'date': date_number}).text
			cours_list_in_bank = json.loads(exchange_rate_page)['exchangeRate']
			for i in cours_list_in_bank:
				if i['currency'] == currency:
					print_rate(date_number, i)


def print_rate(date, rate_dict):
	print(f" {date:12} {rate_dict['currency']:8} {rate_dict['purchaseRateNB']:9} {rate_dict['saleRateNB']:10} ")


def check_correct_date(day, month, year):
	if 1 <= int(day) <= 31 and 1 <= int(month) <= 12 and 2018 <= int(year) <= 2022:
		return True
	else:
		return False


def get_date():
	try:
		day = input("Введіть день (число від 1 до 31):")
		month = input("Введіть місяць (число від 1 до 12):")
		year = input("Введіть рік (число від 2018 до 2022):")
		date = datetime.strptime(year+'.'+month+'.'+day, '%Y.%m.%d')
	except ValueError:
		print("Не коректно введені дані! Такої дати не існує!")
	else:
		if check_correct_date(day, month, year):
			return date
		else:
			return False


def menu_for_users():
	instructions = f"""
	Шановний клієнте!
	Ви можете переглянути курси таких валют:

			USD		долар США
			EUR		євро
			CHF		швейцарський франк
			GBP		британський фунт
			PLZ		польський злотий
			SEK		шведська крона
			XAU		золото
			CAD		канадський долар

	За останні чотири роки. Тобто починаючи з {(datetime.now() - timedelta(days=1459)).strftime('%d/%m/%Y')}

	Натисніть 1  --  Якщо хочете обрати конкретний день
	Натисніть 2  --  Якщо хочете вказати період
	Натисніть 3  --  Якщо бажаєте завершити роботу з програмою

	"""
	print(instructions)
	period = input("Введіть значення:")
	if period == '1':
		start_date = get_date()
		end_date = start_date
		if start_date:
			print("Доступні для перегляду:  USD, EUR, CHF, GBP, PLZ, SEK, XAU, CAD")
			currency = input("Введіть назву валюти з перерахованих вище:")
			if currency in ['USD', 'EUR', 'CHF', 'GBP', 'PLZ', 'SEK', 'XAU', 'CAD']:
				my_ex = ExchangeRateParser()
				my_ex.get_exchange_rate(start_date, end_date, currency)
			else:
				print('Не правильно введене значення!!!')
	elif period == '2':
		print("Введіть дані першого дня бажаного періоду:")
		start_date = get_date()
		print("Введіть дані останнього дня бажаного періоду:")
		end_date = get_date()
		if start_date and end_date:
			print("Доступні для перегляду:  USD, EUR, CHF, GBP, PLZ, SEK, XAU, CAD")
			currency = input("Введіть назву валюти з перерахованих вище:")
			if currency in ['USD', 'EUR', 'CHF', 'GBP', 'PLZ', 'SEK', 'XAU', 'CAD']:
				my_ex = ExchangeRateParser()
				my_ex.get_exchange_rate(start_date, end_date, currency)
			else:
				print('Не правильно введене значення!!!')
	

menu_for_users()
