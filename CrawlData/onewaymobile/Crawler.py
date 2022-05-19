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
        'page1': 'https://onewaymobile.vn/iphone-pc29.html',
        'page2': 'https://onewaymobile.vn/iphone-pc29-page2.html',
        'page3': 'https://onewaymobile.vn/iphone-pc29-page3.html',
        'page4': 'https://onewaymobile.vn/iphone-pc29-page4.html'
    }

    for category in apple_categories:    
        driver.get(apple_categories[category])
        items = driver.find_elements(By.CLASS_NAME, 'title-product')
        for item in items:
            urls.append(item.find_element(By.TAG_NAME,'a').get_attribute('href'))

    for url in tqdm(urls):
        driver.get(url)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[6]/div[1]/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/p/a').click()
        table = driver.find_elements(By.CLASS_NAME,'shop_attributes')[1]
        th = table.find_elements(By.TAG_NAME,'th')
        p = table.find_elements(By.TAG_NAME, 'p')


        product = {}

        price = driver.find_element(By.CLASS_NAME,'price-main').get_attribute('innerHTML')
        name = driver.find_element(By.CLASS_NAME, 'title-book').get_attribute('innerHTML')

        product['name'] = name
        product['url'] = url
        product['price'] = price

        for i in range(0,len(th)):
            product[th[i].get_attribute('innerHTML')] = p[i].get_attribute('innerHTML')
            

        for i in driver.find_element(By.ID, 'temp-oneway').find_elements(By.TAG_NAME, 'span'):
            _product = product.copy()
            _product['color'] = i.get_attribute('style')
            _product['date'] = date
            products.append(_product)

    json_products = json.dumps(products)
    with open("/home/sonnh/Documents/THDL/Data-Integration-20212/CrawlData/onewaymobile/Data.json",'w') as f:
        f.write(json_products)
        f.close()
    driver.quit()