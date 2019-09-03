# -*- coding: utf-8 -*-
import scrapy
from prueba.items import PruebaItem

class CoderSpider(scrapy.Spider):
    name = 'coder'
    allowed_domains = ['coder.mx']
    start_urls = ['https://coder.mx/menu.html']

    def parse(self, response):
        item = PruebaItem()
        item['platillo'] = response.xpath('//dt').extract()
        item['precio'] = response.css('.precio').extract()
        return item