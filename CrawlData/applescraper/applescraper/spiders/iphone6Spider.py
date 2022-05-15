import numpy as np
import scrapy

class IphoneScraper(scrapy.Spider):
    name = 'didongmango'
    start_urls = ['https://didongmango.com/iphone-pc49.html']

    def parse(self, response):
        phone_links = response.xpath('//div[@class="item"]/div/figure/a/@href').getall()

        yield from response.follow_all(phone_links, self.parse_phone)

    def parse_phone(self, response): 
        price = response.xpath('//*[@id="price"]/text()').getall()
        price = [x.replace('\r','').replace('\n','').replace('\t','') for x in price]
        color = response.xpath('//*[@class="color_name"]/text()').getall()
        color = [x.replace('\r','').replace('\n','').replace('\t','') for x in color]
        price_color = response.xpath('//*[@class="price_follow_color"]/text()').getall()
        price_color = [x.replace('\r','').replace('\n','').replace('\t','') for x in price_color]
        

        yield {
            'Name': response.xpath('/html/body/div[11]/div[1]/div[3]/div[1]/div[1]/h1/text()').get().replace('\r','').replace('\n','').replace('\t',''),
            'Price': price,
            'Screen': response.xpath('/html/body/div[11]/div[1]/div[3]/div[3]/div[2]/div[1]/div[2]/div[2]/table/tr[3]/td[2]/text()').get().replace('\r','').replace('\n','').replace('\t','') ,
            'ROM': response.xpath('//*[@id="charactestic_detail"]/div/div[2]/div[2]/table/tr[15]/td[2]/text()').get().replace('\r','').replace('\n','').replace('\t','') ,
            'OS': response.xpath('/html/body/div[11]/div[1]/div[3]/div[3]/div[2]/div[1]/div[2]/div[2]/table/tr[1]/td[2]/text()').get().replace('\r','').replace('\n','').replace('\t','') ,
            'Chipset': response.xpath('//*[@id="charactestic_detail"]/div/div[2]/div[2]/table/tr[12]/td[2]/text()').get().replace('\r','').replace('\n','').replace('\t','') ,
            'size': response.xpath('//*[@id="charactestic_detail"]/div/div[2]/div[2]/table/tr[18]/td[2]/text()').get().replace('\r','').replace('\n','').replace('\t','') ,
            'Color':  str(color),
            'Price_color': str(price_color),
            'Rear camera': response.xpath('//*[@id="charactestic_detail"]/div/div[2]/div[2]/table/tr[7]/td[2]/text()').get().replace('\r','').replace('\n','').replace('\t','') , 
            'Front camera': response.xpath('//*[@id="charactestic_detail"]/div/div[2]/div[2]/table/tr[8]/td[2]/text()').get().replace('\r','').replace('\n','').replace('\t','') ,
            'RAM': response.xpath('//*[@id="charactestic_detail"]/div/div[2]/div[2]/table/tr[13]/td[2]/text()').get().replace('\r','').replace('\n','').replace('\t','') ,
            'Weight': response.xpath('//*[@id="charactestic_detail"]/div/div[2]/div[2]/table/tr[19]/td[2]/text()').get().replace('\r','').replace('\n','').replace('\t','') ,
            'Battery': response.xpath('//*[@id="charactestic_detail"]/div/div[2]/div[2]/table/tr[21]/td[2]/text()').get().replace('\r','').replace('\n','').replace('\t','') ,
            'Sim': response.xpath('//*[@id="charactestic_detail"]/div/div[2]/div[2]/table/tr[24]/td[2]/text()').get().replace('\r','').replace('\n','').replace('\t','') ,
            'link': response.request.url,
            'Language': response.xpath('/html/body/div[11]/div[1]/div[3]/div[3]/div[2]/div[1]/div[2]/div[2]/table/tr[2]/td[2]/text()').get().replace('\r','').replace('\n','').replace('\t','')
        }
