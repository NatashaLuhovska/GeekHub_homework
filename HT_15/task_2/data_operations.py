'''
- data_operations.py з класами CsvOperations та DataBaseOperations. 
CsvOperations містить метод для читання даних. Метод для читання приймає аргументом шлях до csv файлу 
де в колонкі ID записані як валідні, так і не валідні id товарів з сайту. DataBaseOperations містить 
метод для запису даних в sqlite3 базу і відповідно приймає дані для запису. Всі інші методи, 
що потрібні для роботи мають бути приватні/захищені.
'''
import csv
import sqlite3


class CsvOperations:

	@staticmethod
	def read_csv(path):
		with open(path, 'r') as file_id:
			data = csv.reader(file_id)
			ids = [row for row in data]
		return ids[1:]


class DataBaseOperations:

	@staticmethod
	def write_to_db(item):
		sqlite_connection = sqlite3.connect('items_rozetka.db')
		cursor = sqlite_connection.cursor()
		cursor.execute("INSERT INTO items (item_id, title, old_price, current_price, href, brand, category) VALUES \
		(?,?,?,?,?,?,?)", (str(item['item_id']), str(item['title']), str(item['old_price']), str(item['current_price']), 
			str(item['href']), str(item['brand']), str(item['category'])))
		sqlite_connection.commit()
		cursor.close()
		sqlite_connection.close()
