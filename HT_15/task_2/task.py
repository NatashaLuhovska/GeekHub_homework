'''
- task.py - головний модуль, який ініціалізує і запускає весь процес.
Суть процесу: читаємо ID товарів з csv файлу, отримуємо необхідні дані і записуємо їх в базу. 
Якщо ID не валідний/немає даних - вивести відповідне повідомлення і перейти до наступного.
'''
from data_operations import CsvOperations, DataBaseOperations
from rozetka_api import RozetkaAPI

if __name__ == '__main__':
	id_items = CsvOperations().read_csv('items_id.csv')
	for id_item in id_items:
		try:
			data_item = RozetkaAPI().get_item_data(id_item)
			if data_item:
				DataBaseOperations().write_to_db(data_item)
		except Exception:
			print(f"Елемента з заданим ID {id_item} не знайдено")
	
