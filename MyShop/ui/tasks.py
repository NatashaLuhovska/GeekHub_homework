from celery import shared_task

from product.models import Product, Category
from ui.models import AddId

from scraper import RozetkaAPI


@shared_task
def add_product(str_id):
    for id_item in AddId.objects.get(id=str_id).string_ids.split(' '):
        try:
            data_item = RozetkaAPI().get_item_data(id_item)
            if data_item:
                category_item = Category.objects.get_or_create(
                    category=data_item['category'],
                    category_title=data_item['category_title']
                )[0]
                Product.objects.update_or_create(
                    product_id=data_item['item_id'],
                    title=data_item['title'],
                    old_price=data_item['old_price'],
                    current_price=data_item['current_price'],
                    href_product=data_item['href'],
                    brand=data_item['brand'],
                    category=category_item,
                    description=data_item['description'],
                )
            print(f"Елемент з заданим ID {id_item} додано(оновлено)")
        except Exception:
            print(f"Елемента з заданим ID {id_item} не знайдено")
    AddId.objects.get(id=str_id).delete()
    return True
