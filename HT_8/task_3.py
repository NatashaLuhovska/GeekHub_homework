'''Програма-банкомат.
   Використовуючи функції створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.CSV>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.TXT>) та 
      історію транзакцій (файл <{username_transactions.JSON>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених 
      даних (введено цифри; знімається не більше, ніж є на рахунку і т.д.).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається. Але якщо захочете реалізувати функціонал додавання 
      нового користувача - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - на початку роботи - логін користувача (програма запитує ім'я/пароль). Якщо вони неправильні - 
      вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити 
      роботу - все на ентузіазмі :))
      - потім - елементарне меню типн:
        Введіть дію:
           1. Подивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив, можете розширювати функціонал, але основне завдання має бути 
      повністю реалізоване :)
    P.S. Увага! Файли мають бути саме вказаних форматів (csv, txt, json відповідно)
    P.S.S. Добре продумайте структуру програми та функцій'''

import csv
import json

'''
users = [
	{'Name': 'Poll', 'Password': '1234'},
	{'Name': 'Peter', 'Password': '9098'},
	{'Name': 'Russ', 'Password': '7654'},
]

with open('users.csv', 'w', newline='') as users_pass:
    crecord = csv.DictWriter(users_pass, ['Name', 'Password'])
    crecord.writeheader()
    crecord.writerows(users)

for user in users:
	name_balance_file = user["Name"] + "_balance.txt"
	with open(name_balance_file, 'wt') as file_balance:
		file_balance.write("0")

'''

def login():
	with open('users.csv', 'r') as users_pass:
		creading = csv.DictReader(users_pass, fieldnames=['Name', 'Password'])
		users = [row for row in creading]
		for i in range(3):
			name = input("Ввведіть ім'я : ")
			password = input("Введіть пароль : ")
			if {'Name': name, 'Password': password} in users:
				print(f"Вітаємо {name}!")
				return name
			else:
				print(f"Не правильно введені дані, у вас лишилося {2 - i} спроби")
		return False


def chek_balance(name):
	name_balance_file = name + "_balance.txt"
	with open(name_balance_file, 'rt') as file_balance:
		balance = file_balance.read()
	return balance


def withdraw_cash(name):
	cash = int(input('Яку суму ви бажаєте зняти \n'))
	balance = int(chek_balance(name))
	if cash > balance:
		print("Сума перевищує ваш поточний баланс на карті.")
		return "Змініть суму, на ту, що не перевищує Ваш баланс. "
	name_balance_file = name + "_balance.txt"
	with open(name_balance_file, 'wt') as file_balance:
		file_balance.write(str(balance - cash))
	name_transactions_file = name + "_transactions.json"
	transaction = {'Withdraw cash' : cash}
	with open(name_transactions_file, 'a') as file_transactions:
		json.dump(transaction,file_transactions)
	return "Операція успішна!"


def top_up_account(name):
	cash = int(input('Яку суму ви бажаєте покласти на рахунок? \n'))
	balance = int(chek_balance(name))
	name_balance_file = name + "_balance.txt"
	with open(name_balance_file, 'wt') as file_balance:
		file_balance.write(str(balance + cash))
	name_transactions_file = name + "_transactions.json"
	transaction = {'Top up account' : cash}
	with open(name_transactions_file, 'a') as file_transactions:
		json.dump(transaction,file_transactions)
	return "Операція успішна!"
	

def start():
	name = login()
	if not name:
		print("Зверніться, будь ласка, в банк, для уточнення ваших даних.")
		return None
	while True:
		print('%%%%%%%%%%%%%%%%%%%%%%%%%%')	
		print("Яку операцію бажаєте виконати?")
		print('**************************')	
		operations = """			
		Зняти готівку      --  Натисніть 1
		Поповнити рахунок  --  Натисніть 2
		Переглянути баланс --  Натисніть 3
		Вийти              --  Натисніть 4 
		"""
		print(operations)
		print('**************************')	
		operation = input()
		if operation == '1':
			print(withdraw_cash(name))
		elif operation == '2':
			print(top_up_account(name))
		elif operation == '3':
			print(f"На вашому рахунку {chek_balance(name)} грн.")
		elif operation == '4':
			print('До нових зустрічей!')
			return "Дякуємо, що Ви обрали наш банк!"
		else:
			print("Не правильно введене значення!")
		print('%%%%%%%%%%%%%%%%%%%%%%%%%%')
	
print(start())

