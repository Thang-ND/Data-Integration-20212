import scrapy 

import numpy as np
import scrapy

class IphoneScraper(scrapy.Spider):
    name = 'tragopdienthoai4'
    start_urls = ['http://tragopdidong.vn/iphone']

    def parse(self, response):
        phone_links = response.xpath('//a[contains(@href, ".html")]/@href').getall()
        phone_links = np.array(phone_links)
        phone_links = np.unique(phone_links)
        phone_links = list(phone_links)

        yield from response.follow_all(phone_links, self.parse_phone)

    def parse_phone(self, response): 
        yield {
            'description': response.xpath('//*[@id="profile"]/div/text()[5]').get(),
            'link': response.request.url
        }
