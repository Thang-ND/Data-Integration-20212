import numpy as np
import scrapy

class IphoneScraper(scrapy.Spider):
    name = 'cellphoneS-ipad'
    start_urls = ['https://cellphones.com.vn/tablet/ipad-pro.html',
    'https://cellphones.com.vn/tablet/ipad-10-2.html',
    'https://cellphones.com.vn/tablet/ipad-air.html',
    'https://cellphones.com.vn/tablet/ipad-mini.html']

    def parse(self, response):
        mac_links = response.xpath('//*[@class="item-product__box-img"]/a/@href').getall()

        yield from response.follow_all(mac_links, self.parse_mac)

    def parse_mac(self, response): 
        ROM_Price = response.xpath('//*[@class="list-linked"]/a/strong/text()').getall()
        price = response.xpath('//*[@class="list-linked"]/a/span/text()').getall()
        color = response.xpath('//*[@id="configurable_swatch_color"]/li/a/p/strong/text()').getall()
        price_color = response.xpath('//*[@id="configurable_swatch_color"]/li/a/p/span/text()').getall()
        

        yield {
            'Name': response.xpath('/html/body/div[1]/div/section/form[1]/div/div[1]/div/div[1]/h1/text()').get(),
            'Price': price,
            'ROM_P': ROM_Price,
            'Screen': response.xpath('//*[@id="tskt"]/tbody/tr[7]/th[2]/text()').get() ,
            'ROM': response.xpath('//*[@id="tskt"]/tbody/tr[7]/th[2]/text()').get() ,
            'OS': response.xpath('//*[@id="tskt"]/tbody/tr[9]/th[2]/text()').get() ,
            'Chipset': response.xpath('//*[@id="tskt"]/tbody/tr[5]/th[2]/text()').get() ,
            'CPU': response.xpath('//*[@id="tskt"]/tbody/tr[12]/th[2]/text()').get(),
            'Screen size': response.xpath('//*[@id="tskt"]/tbody/tr[1]/th[2]/text()').get() ,
            'Type of Screen': response.xpath('//*[@id="tskt"]/tbody/tr[2]/th[2]/text()').get() ,
            'Color':  str(color),
            'Price_color': str(price_color),
            'Screen resolution': response.xpath('//*[@id="tskt"]/tbody/tr[10]/th[2]/text()').get() ,
            'Screen size': response.xpath('//*[@id="tskt"]/tbody/tr[1]/th[2]/text()').get() ,
            'Functional screen': response.xpath('//*[@id="tskt"]/tbody/tr[11]/th[2]/text()').get(),
            'Rear camera': response.xpath('//*[@id="tskt"]/tbody/tr[3]/th[2]/text()').get(),
            'Front camera': response.xpath('//*[@id="tskt"]/tbody/tr[4]/th[2]/text()').get(),
            'RAM': response.xpath('//*[@id="tskt"]/tbody/tr[6]/th[2]/text()').get() ,
            'Weight': response.xpath('//*[@id="tskt"]/tbody/tr[13]/th[2]/text()').get() ,
            'Battery': response.xpath('//*[@id="tskt"]/tbody/tr[8]/th[2]/text()').get() ,
            'Bluetooth': response.xpath('//*[@id="tskt"]/tbody/tr[14]/th[2]/text()').get() ,
            'Wifi': response.xpath('//*[@id="technicalInfoModal"]/div/div/div[2]/div/div[7]/div[2]/table/tbody/tr[3]/th[2]/text()').get(),
            'Material': response.xpath('//*[@id="technicalInfoModal"]/div/div/div[2]/div/div[8]/div[2]/table/tbody/tr[4]/th[2]/text()').get(),
            'Sound technology': response.xpath('//*[@id="technicalInfoModal"]/div/div/div[2]/div/div[8]/div[2]/table/tbody/tr/th[2]/text()').get(),
            'link': response.request.url
        }
