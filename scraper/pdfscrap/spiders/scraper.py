# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from pdfscrap.items import PdfscrapItem

class ExampleSpider(scrapy.Spider):
    name = 'mobility_scraper'

    # allowed_domains = ['www.google.com']

    start_urls = ['https://www.google.com/covid19/mobility/']

    def parse(self, response):
        for link in response.xpath('//*[@id="glue-filter-result-container"]/div[2]//div[@class="country-data"]//a[contains(@href,".pdf")]//@href').extract():
            print('*'*20,link)
            # print('*'*20,response.url())
            
            
            loader = ItemLoader(item=PdfscrapItem(), selector=link)
            loader.add_value('file_urls', link)
            yield loader.load_item()

            # item = PdfscrapItem()
            # item['file_urls'] = [link]
            # yield item