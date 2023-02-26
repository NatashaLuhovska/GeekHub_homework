import requests
import django
django.setup()


class RozetkaAPI:
    BASE_URL = 'https://rozetka.com.ua/api/product-api/v4/goods/get-main?front-type=xl&country=UA&lang=ua&goodsId='

    def get_item_data(self, elem_id):
        product_url = self.BASE_URL + f'{elem_id}'
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
        item['category_title'] = data.get('last_category')['title']
        item['description'] = data.get('docket')
        return item
