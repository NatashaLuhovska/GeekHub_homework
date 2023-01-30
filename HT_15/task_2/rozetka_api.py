'''
- rozetka_api.py, де створти клас RozetkaAPI, який буде містити 1 метод get_item_data, 
який на вхід отримує id товара з сайту розетки та повертає словник з такими даними: item_id 
(він же і приймається на вхід), title, old_price, current_price, href (лінка на цей товар на сайті), brand, category. 
Всі інші методи, що потрібні для роботи мають бути приватні/захищені.
'''
import requests


class RozetkaAPI:
	BASE_URL = 'https://rozetka.com.ua/api/product-api/v4/goods/get-main?front-type=xl&country=UA&lang=ua&goodsId='

	def get_item_data(self, elem_id):
		product_url = self.BASE_URL + f'{elem_id[0]}'
		page = requests.get(product_url)
		data = page.json().get('data')
		item = dict()
		item['item_id'] = data.get('id')
		item['title'] = data.get('title')
		item['old_price'] = data.get('old_price')
		item['current_price'] = data.get('price')
		item['href'] = data.get('href')
		item['brand'] = data.get('brand')
		item['category'] = data.get('category_id')
		#item['category_title'] = data.get('last_category')['title']
		print(item)
		return item
