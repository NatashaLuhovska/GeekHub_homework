import scrapy
import re


class RozetkaSpider(scrapy.Spider):
    name = 'rozetka'
    allowed_domains = ['rozetka.com.ua']
    BASE_URL = 'http://rozetka.com.ua/ua/'
    #ITEM_URL = 'https://rozetka.com.ua/api/product-api/v4/goods/get-main?front-type=xl&country=UA&lang=ua&goodsId='

    def __init__(self, category):
        self.category = category

    def start_requests(self):
        start_urls = self.BASE_URL + self.category
        yield scrapy.Request(url=start_urls, callback=self.category_parse)

    def category_parse(self, response):
        links_to_item = response.css('a.goods-tile__picture.''ng-star-inserted::attr(href)').getall()
        for link in links_to_item:
            yield scrapy.Request(url=link, callback=self.item_parse)
        number_of_page = int(response.css("a.pagination__link.""ng-star-inserted::text").getall()[-1])
        for page in range(2, number_of_page+1):
            urls = self.BASE_URL + self.category + f'page={page}/'
            yield scrapy.Request(url=urls, callback=self.category_parse)

    def item_parse(self, response):
        item = {'item_id': response.url.split('/')[-2],
                'title': response.css("h1.product__title::text").get(),
                'raiting': response.css("a.product__rating-reviews.""ng-star-inserted::text").get(),
                'description': response.css("p.product-about__brief.""ng-star-inserted::text").get(),
                'price': re.sub(r'[^0-9]', '',response.css("p.product-prices__big::text").get()),
                'href': response.url
                }
        yield item

