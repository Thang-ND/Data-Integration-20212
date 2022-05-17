import numpy as np
import scrapy

class IphoneScraper(scrapy.Spider):
    name = 'viettablet_tablet'
    f = open("../../viettablet/url_ipad.txt", "r")
    start_urls = f.readlines()
    print(start_urls)

    def parse(self, response):
        #phone_links = response.xpath('//div[contains(@class, "product_list_column5")]/div/div[2]/a/@href').getall()
        yield {
           "Name": response.xpath('//*[@id="thong_tin_san_pham"]/div/div[2]/div/form/div/div/div[1]/h1/text()').get(),
           "Price": response.xpath('//*[contains(@id, "sec_discounted_price")]/text()').getall(),
           "Color": response.xpath('//*[contains(@id, "option_description")]/text()').getall(),
           "Data": response.xpath('//ul[@class="no-markers no-margin"]/text()').getall(),
           "link": response.request.url
        } 

    # def parse_phone(self, response): 