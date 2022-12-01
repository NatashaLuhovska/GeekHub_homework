'''Створіть програму для отримання курсу валют за певний період.
- отримати від користувача дату (це може бути як один день так і інтервал - початкова і кінцева дати, 
продумайте механізм реалізації) і назву валюти
- вивести курс по відношенню до гривні на момент вказаної дати (або за кожен день у вказаному інтервалі)
- не забудьте перевірку на валідність введених даних'''

from urllib.parse import urljoin
import requests

from datetime import timedelta, datetime


class ExchangeRateParser:
	BASE_URL = 'https://api.privatbank.ua/'
	IN_BANK_RATE_URL = urljoin(BASE_URL, 'p24api/exchange_rates')


	def get_exchange_rate(self, start_date, end_date, currency):
		day_count = (end_date - start_date).days + 1
		print(f" Дата        Валюта      Купівля    Продаж ")
		for single_date in [d for d in (start_date + timedelta(n) for n in range(day_count)) if d <= end_date]:
			date_number = single_date.strftime('%d.%m.%Y')
			exchange_rate_page = requests.get(self.IN_BANK_RATE_URL, {'date': date_number})
			cours_list_in_bank = exchange_rate_page.json()['exchangeRate']
			flag = True
			for i in cours_list_in_bank:
				if i['currency'] == currency:
					self.print_rate(date_number, i)
					flag = False
					break
			if flag:
				print(date_number, f"Дані за цей день за обраною валютою({currency}) відсутні.")

	@staticmethod
	def print_rate(date, rate_dict):
		print(f" {date:12} {rate_dict['currency']:8} {rate_dict['purchaseRateNB']:9} {rate_dict['saleRateNB']:10} ")

	@staticmethod
	def get_date():
		try:
			print("Введіть дату у форматі: рік.місяць.день (дані вказуйте через крапку)")
			print("Приклад запису дати: 20.10.2020")
			day = input("")
			date = datetime.strptime(day, '%d.%m.%Y')
		except ValueError:
			print("Не коректно введені дані! Такої дати не існує!")
		else:
			date_ch = datetime.now() - timedelta(days=1459)
			if date > date_ch:
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
			PLN		польський злотий
			SEK		шведська крона
			XAU		золото
			CAD		канадський долар

	За останні чотири роки. Тобто починаючи з {(datetime.now() - timedelta(days=1459)).strftime('%d/%m/%Y')}

	Натисніть 1  --  Якщо хочете обрати конкретний день
	Натисніть 2  --  Якщо хочете вказати період
	Натисніть 3  --  Якщо бажаєте завершити роботу з програмою

	"""
	print(instructions)
	exchange = ExchangeRateParser()
	period = input("Введіть значення:")
	if period == '1':
		start_date = exchange.get_date()
		end_date = start_date
		if start_date:
			print("Доступні для перегляду:  USD, EUR, CHF, GBP, PLN, SEK, XAU, CAD")
			currency = input("Введіть назву валюти з перерахованих вище:")
			if currency in ['USD', 'EUR', 'CHF', 'GBP', 'PLN', 'SEK', 'XAU', 'CAD']:
				exchange.get_exchange_rate(start_date, end_date, currency)
			else:
				print('Не правильно введене значення!!!')
		else:
			print("Ви вийшли за рамки вказаного періоду.")
	elif period == '2':
		print("Введіть дані першого дня бажаного періоду:")
		start_date = exchange.get_date()
		print("Введіть дані останнього дня бажаного періоду:")
		end_date = exchange.get_date()
		if start_date and end_date:
			print("Доступні для перегляду:  USD, EUR, CHF, GBP, PLN, SEK, XAU, CAD")
			currency = input("Введіть назву валюти з перерахованих вище:")
			if currency in ['USD', 'EUR', 'CHF', 'GBP', 'PLN', 'SEK', 'XAU', 'CAD']:
				exchange.get_exchange_rate(start_date, end_date, currency)
			else:
				print('Не правильно введене значення!!!')
		else:
			print("Ви вийшли за рамки вказаного періоду.")
	elif period == '3':
		print("До зустрічі!")
	else:
		print("Не коректно введені значення!!!")
	

menu_for_users()
