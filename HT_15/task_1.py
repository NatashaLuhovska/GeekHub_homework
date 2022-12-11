'''
Викорисовуючи requests/BeautifulSoup, заходите на ось цей сайт "https://www.expireddomains.net/domain-lists/" 
(з ним будьте обережні :подмигивание::череп_и_кости:), вибираєте будь-яку на ваш вибір доменну зону і парсите 
список  доменів з усіма відповідними колонками - доменів там буде десятки тисяч (звичайно ураховуючи пагінацію). 
Всі отримані значення зберегти в CSV файл.
'''

import csv
from dataclasses import dataclass, fields, astuple
from time import sleep
from random import randrange

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


@dataclass
class Domain:
    domain: str
    BL: str
    DP: str
    ABY: str
    ACR: str
    Dmoz: str
    C: str
    N: str
    O: str
    D: str
    Reg: str
    RDT: str
    Traffic: str
    Valuation: str
    Price: str


class SiteDomainsParser:
    BASE_URL = 'https://www.expireddomains.net/godaddy-closeout-domains/'
    DOMAIN_FIELDS = [field.name for field in fields(Domain)]
    DOMAIN_OUTPUT_CSV_PATH = 'domains.csv'

    def get_site_domains(self) -> [Domain]:
        with requests.Session() as session:
            page = session.get(self.BASE_URL, headers={'user-agent': UserAgent().chrome}).content
            first_page_soup = BeautifulSoup(page, 'lxml')
            print('Get data from first page')
            all_domains = self.get_single_page_domains(first_page_soup)
            for page_number in range(25, 301, 25):
                sleep(randrange(5, 13))
                print(f'Get data from start {page_number}')
                page = session.get(self.BASE_URL, params={'start': int(page_number)}, headers={'user-agent': UserAgent().chrome}).content
                soup = BeautifulSoup(page, 'lxml')
                all_domains.extend(self.get_single_page_domains(soup))
            return all_domains

    def get_single_page_domains(self, page_soup: BeautifulSoup) -> [Domain]:
        domains = page_soup.select('tbody tr')
        return [self.parse_single_domain(domain_soup) for domain_soup in domains]
       
    def parse_single_domain(self, domain_soup: BeautifulSoup) -> Domain:
        return Domain(
            domain=domain_soup.select_one('.field_domain a')['title'],
            BL=domain_soup.select_one('.field_bl a')['title'],
            DP=domain_soup.select_one('.field_domainpop a')['title'],
            ABY=domain_soup.select_one('.field_abirth').text,
            ACR=domain_soup.select_one('.field_aentries a').text,
            Dmoz=domain_soup.select_one('.field_dmoz').text,
            C=domain_soup.select_one('.field_statuscom span').text,
            N=domain_soup.select_one('.field_statusnet span').text,
            O=domain_soup.select_one('.field_statusorg span').text,
            D=domain_soup.select_one('.field_statusde span').text,
            Reg=domain_soup.select_one('.field_statustld_registered').text,
            RDT=domain_soup.select_one('.field_related_cnobi').text,
            Traffic=domain_soup.select_one('.field_traffic a').text,
            Valuation=domain_soup.select_one('.field_valuation a').text,
            Price=domain_soup.select_one('.field_price a').text
                )

    def write_domains_to_csv(self, domains: [Domain]):
        with open(self.DOMAIN_OUTPUT_CSV_PATH, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(self.DOMAIN_FIELDS)
            writer.writerows([astuple(domain) for domain in domains])
        return


if __name__ == '__main__':
    parser = SiteDomainsParser()
    site_domains = parser.get_site_domains()
    parser.write_domains_to_csv(site_domains)

