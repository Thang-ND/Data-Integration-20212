import numpy as np
import scrapy

class IphoneScraper(scrapy.Spider):
    name = 'tragopdienthoai3'
    start_urls = ['http://tragopdidong.vn/iphone']

    def parse(self, response):
        phone_links = response.xpath('//a[contains(@href, ".html")]/@href').getall()
        phone_links = np.array(phone_links)
        phone_links = np.unique(phone_links)
        phone_links = list(phone_links)

        yield from response.follow_all(phone_links, self.parse_phone)

    def parse_phone(self, response): 
        yield {
            'Screen': response.xpath('//*[@id="profile"]/div/ul[2]/li[2]/text()').get() ,
            'camera': response.xpath('//*[@id="profile"]/div/ul[1]/li[3]/span/text()').get() ,
            'ROM': response.xpath('//*[@id="profile"]/div/ul[17]/li[2]/text()').get() ,
            'OS': response.xpath('//*[@id="profile"]/div/ul[12]/li[2]/text()').get() ,
            'Chipset': response.xpath('//*[@id="profile"]/div/ul[13]/li[2]/text()').get() ,
            'GPU': response.xpath('//*[@id="profile"]/div/ul[15]/li[1]/text()').get() ,
            'size': response.xpath('//*[@id="profile"]/div/ul[30]/li[2]/text()').get() ,
            'Type of Screen': response.xpath('//*[@id="profile"]/div/ul[1]/li[2]/text()').get() ,
            'Color': response.xpath('//*[@id="profile"]/div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/text()').get() ,
            'Standard screen': response.xpath('//*[@id="profile"]/div/ul[1]/li[2]/text()').get() ,
            'Screen resolution': response.xpath('//*[@id="profile"]/div/table/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[2]/text()').get() ,
            'Screen size': response.xpath('//*[@id="profile"]/div/ul[3]/li[2]/text()').get() ,
            'Touch': response.xpath('//*[@id="profile"]/div/table/tbody/tr[2]/td[2]/table/tbody/tr[6]/td[2]/text()').get() ,
            'Rear camera': response.xpath('//*[@id="profile"]/div/ul[5]/li[2]/text()').get() , 
            'Front camera': response.xpath('//*[@id="profile"]/div/ul[9]/li[2]/text()').get() ,
            'Flash': response.xpath('//*[@id="profile"]/div/ul[7]/li[2]/text()').get() ,
            'Functional camera': response.xpath('//*[@id="profile"]/div/ul[8]/li[2]/text()').get() ,
            'Video': response.xpath('//*[@id="profile"]/div/ul[6]/li[2]/text()').get() ,
            'Video call': response.xpath('//*[@id="profile"]/div/table/tbody/tr[3]/td[2]/table/tbody/tr[6]/td[2]/text()').get() ,
            'Cores': response.xpath('//*[@id="profile"]/div/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td[2]/text()').get() ,
            'RAM': response.xpath('//*[@id="profile"]/div/ul[16]/li[2]/text()').get() ,
            'SD': response.xpath('//*[@id="profile"]/div/ul[19]/li[2]/text()').get() ,
            'Style': response.xpath('//*[@id="profile"]/div/ul[29]/li[2]/text()').get() ,
            'Weight': response.xpath('//*[@id="profile"]/div/ul[31]/li[2]/text()').get() ,
            'Battery': response.xpath('//*[@id="profile"]/div/ul[32]/li[2]/text()').get() ,
            '2G': response.xpath('//*[@id="profile"]/div/ul[20]/li[2]/text()').get() ,
            '3G': response.xpath('//*[@id="profile"]/div/ul[20]/li[2]/text()').get() ,
            '4G': response.xpath('//*[@id="profile"]/div/ul[20]/li[2]/text()').get() ,
            'Support sim': response.xpath('//*[@id="profile"]/div/table/tbody/tr[8]/td[2]/table/tbody/tr[3]/td[2]/text()').get() ,
            'Sim': response.xpath('//*[@id="profile"]/div/ul[21]/li[2]/text()').get() ,
            'Wifi': response.xpath('//*[@id="profile"]/div/ul[22]/li[2]/text()').get() ,
            'GPS': response.xpath('//*[@id="profile"]/div/ul[23]/li[2]/text()').get() ,
            'Bluetooth': response.xpath('//*[@id="profile"]/div/ul[24]/li[2]/text()').get() ,
            'link': response.request.url
        }
