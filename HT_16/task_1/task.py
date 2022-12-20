'''1. Використовуючи Scrapy, заходите на "https://chrome.google.com/webstore/sitemap", 
переходите на кожен лінк з тегів <loc>, з кожного лінка берете посилання на сторінки 
екстеншинів, парсите їх і зберігаєте в CSV файл ID, назву та короткий опис кожного 
екстеншена (пошукайте уважно де його можна взяти). Наприклад:
“aapbdbdomjkkjkaonfhkkikfgjllcleb”, “Google Translate”, 
“View translations easily as you browse the web. By the Google Translate team.”'''

from scrapy.crawler import CrawlerProcess

from extensions.extensions.spiders.extensions_spider import ExtensionsSpiderSpider


if __name__ == '__main__':
    craw_process = CrawlerProcess(settings={
    "FEEDS": {
        "extensions_info.csv": {
        "format": "csv",
        "header": True
        },
    },
    })
    craw_process.crawl(ExtensionsSpiderSpider)
    craw_process.start()