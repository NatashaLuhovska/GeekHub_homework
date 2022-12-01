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
    HOME_URL = urljoin(BASE_URL, 'page/1/')
    QUOTE_FIELDS = [field.name for field in fields(Quote)]
    QUOTE_OUTPUT_CSV_PATH = 'quotes.csv'

    def get_site_quotes(self) -> [Quote]:
        page = requests.get(self.HOME_URL).content
        first_page_soup = BeautifulSoup(page, 'lxml')
        print('Get data from first page')
        all_quotes = self.get_single_page_quotes(first_page_soup)
        for page_number in range(2, 11):
            print(f'Get data from page {page_number}')
            page = requests.get(self.HOME_URL, f'page/{page_number}/').content
            soup = BeautifulSoup(page, 'lxml')
            all_quotes.extend(self.get_single_page_quotes(soup))
        return all_quotes

    def get_single_page_quotes(self, page_soup: BeautifulSoup) -> [Quote]:
        quotes = page_soup.select('.quote')
        return [self.parse_single_quote(quote_soup) for quote_soup in quotes]
       
    def parse_single_quote(self, quote_soup: BeautifulSoup) -> Quote:
        return Quote(
            quote=quote_soup.select_one('.text').text,
            author=quote_soup.select_one('.author').text,
            tags=quote_soup.select_one('.keywords')['content'],
            born_date=self.get_site_about_author(quote_soup,'.author-born-date'),
            born_location=self.get_site_about_author(quote_soup, '.author-born-location'),
            description_author=self.get_site_about_author(quote_soup, '.author-description')
        )

    def write_quotes_to_csv(self, quotes: [Quote]):
        with open(self.QUOTE_OUTPUT_CSV_PATH, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(self.QUOTE_FIELDS)
            writer.writerows([astuple(quote) for quote in quotes])
        return

    def get_site_about_author(self, quote_soup: BeautifulSoup, tag: str) -> str:
        author_url = urljoin(self.BASE_URL, quote_soup.select_one('span > a')['href'])
        author_page = requests.get(author_url).content
        author_page_soup = BeautifulSoup(author_page, 'lxml')
        return author_page_soup.select_one(tag).text


if __name__ == '__main__':
    parser = SiteQuotesParser()
    site_quotes = parser.get_site_quotes()
    parser.write_quotes_to_csv(site_quotes)
