'''2. Викорисовуючи Scrapy, написати скрипт, який буде приймати на вхід назву та ID категорії 
(у форматі назва/id/) із сайту https://rozetka.com.ua і буде збирати всі товари із цієї 
категорії, збирати по ним всі можливі дані (бренд, категорія, модель, ціна, рейтинг тощо) і 
зберігати їх у CSV файл (наприклад, якщо передана категорія mobile-phones/c80003/, то файл 
буде називатися c80003_products.csv)'''


from scrapy.crawler import CrawlerProcess

from rozetka_api.rozetka_api.spiders.rozetka import RozetkaSpider


if __name__ == '__main__':
    category = 'notebooks/c80004/'
    craw_process = CrawlerProcess(settings={
    "FEEDS": {
        f"{category.split('/')[-2]}_products.csv": {
        "format": "csv",
        "header": True
        },
    },
    })
    craw_process.crawl(RozetkaSpider, category=category)
    craw_process.start()

