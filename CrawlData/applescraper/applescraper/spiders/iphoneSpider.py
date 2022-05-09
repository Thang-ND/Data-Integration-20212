import numpy as np
import scrapy

class IphoneScraper(scrapy.Spider):
    name = 'tragopdienthoai'
    start_urls = ['http://tragopdidong.vn/iphone']

    def parse(self, response):
        phone_links = products = response.xpath('//a[contains(@href, ".html")]/@href').getall()
        phone_links = np.array(phone_links)
        phone_links = np.unique(phone_links)
        phone_links = list(phone_links)

        yield from response.follow_all(phone_links, self.parse_phone)

    def parse_phone(self, response): 
        yield {
            'Screen': response.xpath('//*[@id="profile"]/div/ul[1]/li[2]/span/text()').get(),
            'camera': response.xpath('//*[@id="profile"]/div/ul[1]/li[3]/span/text()').get(),
            'ROM': response.xpath('//*[@id="profile"]/div/ul[1]/li[4]/span/text()').get(),
            'OS': response.xpath('//*[@id="profile"]/div/ul[1]/li[5]/span/text()').get(),
            'Chipset': response.xpath('//*[@id="profile"]/div/ul[1]/li[6]/span/text()').get(),
            'GPU': response.xpath('//*[@id="profile"]/div/ul[1]/li[7]/span/text()').get(),
            'size': response.xpath('//*[@id="profile"]/div/ul[1]/li[8]/span/text()').get(),
            'Type of Screen': response.xpath('//*[@id="profile"]/div/ul[2]/li[2]/span/text()').get(),
            'Color': response.xpath('//*[@id="profile"]/div/ul[2]/li[3]/span/text()').get(),
            'Standard screen': response.xpath('//*[@id="profile"]/div/ul[2]/li[4]/span/text()').get(),
            'Screen resolution': response.xpath('//*[@id="profile"]/div/ul[2]/li[5]/span/text()').get(),
            'Screen size': response.xpath('//*[@id="profile"]/div/ul[2]/li[6]/span/text()').get(),
            'Touch': response.xpath('//*[@id="profile"]/div/ul[2]/li[7]/span/text()').get(),
            'Rear camera': response.xpath('//*[@id="profile"]/div/ul[2]/li[9]/span/text()').get(), 
            'Front camera': response.xpath('//*[@id="profile"]/div/ul[2]/li[10]/span/text()').get(),
            'Flash': response.xpath('//*[@id="profile"]/div/ul[2]/li[11]/span/text()').get(),
            'Functional camera': response.xpath('//*[@id="profile"]/div/ul[2]/li[12]/span/text()').get(),
            'Video': response.xpath('//*[@id="profile"]/div/ul[2]/li[13]/span/text()').get(),
            'Video call': response.xpath('//*[@id="profile"]/div/ul[2]/li[14]/span/text()').get(),
            'Cores': response.xpath('//*[@id="profile"]/div/ul[2]/li[16]/span/text()').get(),
            'RAM': response.xpath('//*[@id="profile"]/div/ul[2]/li[18]/span/text()').get(),
            'SD': response.xpath('//*[@id="profile"]/div/ul[2]/li[23]/span/text()').get(),
            'Style': response.xpath('//*[@id="profile"]/div/ul[2]/li[26]/span/text()').get(),
            'Weight': response.xpath('//*[@id="profile"]/div/ul[2]/li[28]/span/text()').get(),
            'Battery': response.xpath('//*[@id="profile"]/div/ul[2]/li[30]/span/text()').get(),
            '2G': response.xpath('//*[@id="profile"]/div/ul[2]/li[33]/span/text()').get(),
            '3G': response.xpath('//*[@id="profile"]/div/ul[2]/li[34]/span/text()').get(),
            '4G': response.xpath('//*[@id="profile"]/div/ul[2]/li[35]/span/text()').get(),
            'Support sim': response.xpath('//*[@id="profile"]/div/ul[2]/li[36]/span/text()').get(),
            'Sim': response.xpath('//*[@id="profile"]/div/ul[2]/li[37]/span/text()').get(),
            'Wifi': response.xpath('//*[@id="profile"]/div/ul[2]/li[38]/span/text()').get(),
            'GPS': response.xpath('//*[@id="profile"]/div/ul[2]/li[39]/span/text()').get(),
            'Bluetooth': response.xpath('//*[@id="profile"]/div/ul[2]/li[40]/span/text()').get(),
        }
