''' http://quotes.toscrape.com/ - написати скрейпер для збору 
всієї доступної інформації про записи: цитата, автор, інфа про автора тощо.
- збирається інформація з 10 сторінок сайту.
- зберігати зібрані дані у CSV файл'''

import csv
from dataclasses import dataclass, fields, astuple
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


@dataclass
class Quote:
    quote: str
    author: str
    tags: str
    born_date: str
    born_location: str
    description_author: str


class SiteQuotesParser:
    BASE_URL = 'http://quotes.toscrape.com/'
    HOME_URL = urljoin(BASE_URL, '/page/1/')
    QUOTE_FIELDS = [field.name for field in fields(Quote)]
    QUOTE_OUTPUT_CSV_PATH = 'quotes.csv'

    def get_site_products(self) -> [Quote]:
        page = requests.get(self.HOME_URL).content
        first_page_soup = BeautifulSoup(page, 'lxml')
        print('Get data from first page')
        all_products = self.get_single_page_quotes(first_page_soup)
        for page_number in range(2, 11):
            print(f'Get data from page {page_number}')
            page = requests.get(self.HOME_URL, f'page/{page_number}/').content
            soup = BeautifulSoup(page, 'lxml')
            all_products.extend(self.get_single_page_quotes(soup))
        return all_products


    def get_single_page_quotes(self, page_soup: BeautifulSoup) -> [Quote]:
        quotes = page_soup.select('.quote')
        return [self.parse_single_quote(quote_soup) for quote_soup in quotes]
       

    @staticmethod
    def parse_single_quote(product_soup: BeautifulSoup) -> Quote:
        return Quote(
            quote=product_soup.select_one('.text').text,
            author=product_soup.select_one('.author').text,
            tags=product_soup.select_one('.keywords')['content'],
            born_date=get_site_about_author(product_soup.select_one('span > a')['href']).select_one('.author-born-date').text,
            born_location=get_site_about_author(product_soup.select_one('span > a')['href']).select_one('.author-born-location').text,
            description_author=get_site_about_author(product_soup.select_one('span > a')['href']).select_one('.author-description').text
        )

    def write_products_to_csv(self, quotes: [Quote]):
        with open(self.QUOTE_OUTPUT_CSV_PATH, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(self.QUOTE_FIELDS)
            writer.writerows([astuple(quote) for quote in quotes])
        return
   
def get_site_about_author(href_author: str) -> BeautifulSoup:
    AUTHOR_URL = urljoin('http://quotes.toscrape.com/', href_author)
    author_page = requests.get(AUTHOR_URL).content
    author_page_soup = BeautifulSoup(author_page, 'lxml')
    return author_page_soup


if __name__ == '__main__':
    parser = SiteQuotesParser()
    site_quotes = parser.get_site_products()
    parser.write_products_to_csv(site_quotes)
