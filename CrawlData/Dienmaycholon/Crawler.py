from math import prod
import time
from attr import attrib
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from tqdm import tqdm
from selenium.webdriver.firefox.options import Options as FirefoxOptions


if __name__ == '__main__':

    today = time.gmtime()
    date = '{}-{}-{}'.format(today.tm_year,today.tm_mon,today.tm_mday)

    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)

    urls = []
    products = []
    apple_categories = {
        'iphone': 'https://dienmaycholon.vn/dien-thoai-di-dong-apple'
    }

    for category in apple_categories:    
        driver.get(apple_categories[category])
        items = driver.find_elements(By.CLASS_NAME, 'product')
        for item in items:
            urls.append(item.get_attribute('href'))

    for url in tqdm(urls):
        driver.get(url)
    
        color = []
        price = []

        for i in driver.find_elements(By.CLASS_NAME, 'size-pro'):
            color.append(i.get_attribute('innerHTML'))
        for i in driver.find_elements(By.CLASS_NAME, 'price-pro'):
            price.append(i.get_attribute('innerHTML'))

        product = {}
        name = driver.find_element(By.CLASS_NAME, 'name_pro_detail').find_element(By.TAG_NAME,'h1').get_attribute('innerHTML')
        product['name'] = name
        product['url'] = url
        div = driver.find_element(By.CLASS_NAME, 'detail_specifications')
        li = div.find_elements(By.TAG_NAME, 'li')
        for item in li:
            p = item.find_elements(By.TAG_NAME, 'p')
            if (len(p)>0):
                attribute = p[0].get_attribute('innerHTML')
                value = p[1].get_attribute('innerHTML')
                product[attribute] = value

        for i in range(0,len(color)):
            _product = product.copy()
            _product['color'] = color[i]
            _product['price'] = price[i]
            _product['date'] = date
            products.append(_product)

    with open('/home/sonnh/Documents/THDL/Data-Integration-20212/CrawlData/Dienmaycholon/Data.json', 'w') as f:
        f.write(json.dumps(products))
        f.close()
    driver.quit()