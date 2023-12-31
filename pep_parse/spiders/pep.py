from urllib.parse import urljoin

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Собирает ссылки на документы PEP"""
        peps = response.css(
            'section[id=numerical-index] tbody a::attr(href)'
        ).getall()
        for link in peps:
            yield response.follow(
                urljoin(self.start_urls[0], link, '/'),
                callback=self.parse_pep
            )

    def parse_pep(self, response):
        """Парсит страницы с документами и формирует Items"""
        name = response.css('h1.page-title::text').get().strip()
        data = {
            'name': name,
            'number': name.split('–')[0].replace('PEP', '').strip(),
            'status': response.css('abbr::text').get()
        }
        yield PepParseItem(data)
