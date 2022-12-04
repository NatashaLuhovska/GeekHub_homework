import csv
from dataclasses import dataclass, fields, astuple
from urllib.parse import urljoin
from fake_useragent import UserAgent

import requests
from bs4 import BeautifulSoup


@dataclass
class Domain:
    quote: str
    author: str
    tags: str
    born_date: str
    born_location: str
    description_author: str


class SiteDomainsParser:
    BASE_URL = 'https://www.expireddomains.net/godaddy-closeout-domains/'
    
    #HOME_URL = urljoin(BASE_URL, 'page/1/')
    DOMAIN_FIELDS = [field.name for field in fields(Domain)]
    DOMAIN_OUTPUT_CSV_PATH = 'domains.csv'



    def get_site_domains(self) -> [Domain]:
    	with requests.Session() as session:
	        page = session.get(self.HOME_URL, headers = {'user-agent': UserAgent().chrome}).content
	        first_page_soup = BeautifulSoup(page, 'lxml')
	        print('Get data from first page')
	        all_domains = self.get_single_page_domains(first_page_soup)
	        for page_number in range(25, 301, 25):
	            print(f'Get data from start {page_number}')
	            page = session.get(self.HOME_URL, {'start': int(start)}, headers = {'user-agent': UserAgent().chrome}).content
	            soup = BeautifulSoup(page, 'lxml')
	            all_domains.extend(self.get_single_page_domains(soup))
	        return all_domains

    def get_single_page_domains(self, page_soup: BeautifulSoup) -> [Domain]:
        domains = page_soup.select('tbody tr')
        return [self.parse_single_domain(domain_soup) for domain_soup in domains]
       
    def parse_single_domain(self, domain_soup: BeautifulSoup) -> Domain:
        return Quote(
            quote=quote_soup.select_one('.text').text,
            author=quote_soup.select_one('.author').text,
            tags=quote_soup.select_one('.keywords')['content'],
            born_date=self.get_site_about_author(quote_soup,'.author-born-date'),
            born_location=self.get_site_about_author(quote_soup, '.author-born-location'),
            description_author=self.get_site_about_author(quote_soup, '.author-description')
        )




if __name__ == '__main__':
    parser = SiteDomainsParser()
    site_quotes = parser.get_site_domains()
