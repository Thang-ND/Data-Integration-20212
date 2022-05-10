import numpy as np
import scrapy

class IphoneScraper(scrapy.Spider):
    name = 'cellphoneS1'
    start_urls = ['https://cellphones.com.vn/mobile/apple/iphone-13.html',
    'https://cellphones.com.vn/mobile/apple/iphone-12-vna.html',
    'https://cellphones.com.vn/mobile/apple/iphone-11-series.html',
    'https://cellphones.com.vn/mobile/apple/iphone-se.html']

    def parse(self, response):
        phone_links = response.xpath('//div[@class="item-product__box-img"]/a/@href').getall()

        yield from response.follow_all(phone_links, self.parse_phone)

    def parse_phone(self, response): 
        ROM_Price = response.xpath('/html/body/div[1]/div/section/form[1]/div/div[2]/div[2]/div[2]/div/a/strong/text()').getall()
        price = response.xpath('/html/body/div[1]/div/section/form[1]/div/div[2]/div[2]/div[2]/div/a/span/text()').getall()
        color = response.xpath('//*[@id="configurable_swatch_color"]/li/a/p/strong/text()').getall()
        price_color = response.xpath('//*[@id="configurable_swatch_color"]/li/a/p/span/text()').getall()
        

        yield {
            'Name': response.xpath('/html/body/div[1]/div/section/form[1]/div/div[1]/div/div[1]/h1/text()').get(),
            'Price': price,
            'ROM_P': ROM_Price,
            'Screen': response.xpath('//*[@id="tskt"]/tbody/tr[2]/th[2]/text()').get() ,
            'camera': response.xpath('//*[@id="profile"]/div/ul[1]/li[3]/span/text()').get() ,
            'ROM': response.xpath('//*[@id="tskt"]/tbody/tr[7]/th[2]/text()').get() ,
            'OS': response.xpath('//*[@id="tskt"]/tbody/tr[10]/th[2]/text()').get() ,
            'Chipset': response.xpath('//*[@id="tskt"]/tbody/tr[5]/th[2]/text()').get() ,
            'GPU': response.xpath('//*[@id="profile"]/div/ul[1]/li[7]/span/text()').get() ,
            'size': response.xpath('//*[@id="profile"]/div/ul[1]/li[8]/span/text()').get() ,
            'Type of Screen': response.xpath('//*[@id="profile"]/div/ul[2]/li[2]/span/text()').get() ,
            'Color':  str(color),
            'Price_color': str(price_color),
            'Screen resolution': response.xpath('//*[@id="tskt"]/tbody/tr[11]/th[2]/text()').get() ,
            'Screen size': response.xpath('//*[@id="tskt"]/tbody/tr[1]/th[2]/text()').get() ,
            'Rear camera': response.xpath('//*[@id="tskt"]/tbody/tr[3]/th[2]/text()').get() , 
            'Front camera': response.xpath('//*[@id="tskt"]/tbody/tr[4]/th[2]/text()').get() ,
            'Functional fullscreen': response.xpath('//*[@id="tskt"]/tbody/tr[12]/th[2]/text()').get() ,
            'RAM': response.xpath('//*[@id="tskt"]/tbody/tr[6]/th[2]/text()').get() ,
            'Weight': response.xpath('//*[@id="tskt"]/tbody/tr[13]/th[2]/text()').get() ,
            'Battery': response.xpath('//*[@id="tskt"]/tbody/tr[8]/th[2]/text()').get() ,
            'Sim': response.xpath('//*[@id="tskt"]/tbody/tr[9]/th[2]/text()').get() ,
            'Bluetooth': response.xpath('//*[@id="tskt"]/tbody/tr[14]/th[2]/text()').get() ,
            'link': response.request.url
        }
