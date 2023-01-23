import requests
import django
django.setup()

from product.models import Product
from ui.models import AddId
from sys import argv


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
        item['description'] = data.get('docket')
        return item


def add_product(id_item):
    try:
        data_item = RozetkaAPI().get_item_data(id_item)
        if data_item:
            Product.objects.update_or_create(
                product_id=data_item['item_id'],
                title=data_item['title'],
                old_price=data_item['old_price'],
                current_price=data_item['current_price'],
                href_product=data_item['href'],
                brand=data_item['brand'],
                category=data_item['category'],
                description=data_item['description'],
            )
    except Exception:
        print(f"Елемента з заданим ID {id_item} не знайдено")


if __name__ == '__main__':
    str_id = argv[1]
    for item_id in AddId.objects.get(id=str_id).string_ids.split(' '):
        add_product(item_id)
    AddId.objects.get(id=str_id).delete()
