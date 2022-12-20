import scrapy


class ExtensionsSpiderSpider(scrapy.Spider):
    name = 'extensions_spider'
    allowed_domains = ['chrome.google.com']

    def start_requests(self):
        start_urls = 'https://chrome.google.com/webstore/sitemap'
        yield scrapy.Request(url=start_urls, callback=self.first_parse)


    def first_parse(self, response):
        links_to_list = response.xpath("//*[name()='loc']/text()").getall()
        for first_link in links_to_list:
            yield scrapy.Request(url=first_link, callback=self.second_parse)

    def second_parse(self, response):
        links_to_extension = response.xpath("//*[name()='loc']/text()").getall()
        for second_link in links_to_extension:
            yield scrapy.Request(url=second_link, callback=self.extention_parse)
    
    @staticmethod
    def extention_parse(response):
        item = {
        'id': response.url.split('/')[-1],
        'name': response.css("h1::text").get(),
        'description': response.css("div.C-b-p-j-Pb::text").get()
        }
        yield item


    