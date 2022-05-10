import numpy as np
import scrapy

class IphoneScraper(scrapy.Spider):
    name = 'cellphoneS-applewatch'
    start_urls = ['https://cellphones.com.vn/do-choi-cong-nghe/apple-watch/series-3.html',
    'https://cellphones.com.vn/do-choi-cong-nghe/apple-watch/series-5.html',
    'https://cellphones.com.vn/do-choi-cong-nghe/apple-watch/series-6.html',
    'https://cellphones.com.vn/do-choi-cong-nghe/apple-watch/series-7.html',
    'https://cellphones.com.vn/do-choi-cong-nghe/apple-watch/se.html']

    def parse(self, response):
        watch_links = response.xpath('//*[@class="item-product__box-img"]/a/@href').getall()

        yield from response.follow_all(watch_links, self.parse_watch)

    def parse_watch(self, response): 
        ROM_Price = response.xpath('//*[@class="list-linked"]/a/strong/text()').getall()
        price = response.xpath('//*[@class="list-linked"]/a/span/text()').getall()
        color = response.xpath('//*[@id="configurable_swatch_color"]/li/a/p/strong/text()').getall()
        price_color = response.xpath('//*[@id="configurable_swatch_color"]/li/a/p/span/text()').getall()
        

        yield {
            'Name': response.xpath('/html/body/div[1]/div/section/form[1]/div/div[1]/div/div[1]/h1/text()').get(),
            'Price': price,
            'ROM_P': ROM_Price,
            'Color':  str(color),
            'Price_color': str(price_color),
            'Diameter': response.xpath('//*[@id="technicalInfoModal"]/div/div/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/th[2]/text()').get(),
            'Screen technology': response.xpath('//*[@id="technicalInfoModal"]/div/div/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/th[2]/text()').get(),
            'Material': response.xpath('//*[@id="technicalInfoModal"]/div/div/div[2]/div/div[1]/div[2]/table/tbody/tr[3]/th[2]/text()').get(),
            'Resiswater technology': response.xpath('//*[@id="technicalInfoModal"]/div/div/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/th[2]/text()').get(),
            'Production': response.xpath('//*[@id="technicalInfoModal"]/div/div/div[2]/div/div[2]/div[2]/table/tbody/tr[2]/th[2]/text()').get(),
            'Battery time': response.xpath('//*[@id="technicalInfoModal"]/div/div/div[2]/div/div[3]/div[2]/table/tbody/tr[1]/th[2]/text()').get(),
            'Charge time': response.xpath('//*[@id="technicalInfoModal"]/div/div/div[2]/div/div[3]/div[2]/table/tbody/tr[2]/th[2]/text()').get(),
            'OS': response.xpath('//*[@id="technicalInfoModal"]/div/div/div[2]/div/div[3]/div[2]/table/tbody/tr[2]/th[2]/text()').get(),
            'Features': response.xpath('//*[@id="technicalInfoModal"]/div/div/div[2]/div/div[5]/div[2]/table/tbody/tr/th[2]/text()').get(),
            'link': response.request.url
        }
