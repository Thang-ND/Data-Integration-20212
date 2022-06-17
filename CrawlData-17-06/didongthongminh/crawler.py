from math import prod
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from tqdm import tqdm
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':

    today = time.gmtime()
    date = '{}-{}-{}'.format(today.tm_year,today.tm_mon,today.tm_mday)

    options = Options()
    options.headless = True

    service = Service(executable_path="D:\THDL\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    urls = []
    products = []
    apple_categories = {
        'iphone': 'https://didongthongminh.vn/iphone'
    }

    for category in apple_categories:
        driver.get(apple_categories[category])
        driver.find_element(By.ID,'load_more_button').click()
        time.sleep(2)
        driver.find_element(By.ID,'load_more_button').click()
        time.sleep(2)
        driver.find_element(By.ID,'load_more_button').click()
        time.sleep(2)
        items = driver.find_elements(By.CLASS_NAME, 'frame_inner')
        for item in items:
            urls.append(item.find_element(By.TAG_NAME,'a').get_attribute('href'))
    

    for url in tqdm(urls):
        product = {}
        driver.get(url)
        colors = []
        prices = [] 

        name = driver.find_element(By.CLASS_NAME, 'pull-left').get_attribute('innerHTML')
        product['name'] = name
        product['url'] = url

        products_type = driver.find_element(By.CLASS_NAME, 'products_type')
        p = products_type.find_elements(By.TAG_NAME, 'p')
        for i in p:
            span = i.find_elements(By.TAG_NAME, 'span')
            colors.append(span[0].get_attribute('innerHTML'))
            prices.append(span[0].get_attribute('innerHTML'))

        product = {}
       
        
        for j in driver.find_elements(By.CLASS_NAME, 'tr-0'):
            td = j.find_elements(By.TAG_NAME, 'td')
            attribute = td[0].get_attribute('innerHTML')
            value = td[1].get_attribute('innerHTML')
            product[attribute] = value
        for j in driver.find_elements(By.CLASS_NAME, 'tr-1'):
            td = j.find_elements(By.TAG_NAME, 'td')
            attribute = td[0].get_attribute('innerHTML')
            value = td[1].get_attribute('innerHTML')
            product[attribute] = value
        for index in range(0,len(colors)):
            _product = product.copy()
            _product['color'] = colors[index]
            _product['price'] = prices[index]
            _product['time'] = date
            products.append(_product)
    print(products)
    with open('D:\THDL\Data-Integration-20212\CrawlData-17-06\didongthongminh\didongthongminh.json', 'w') as f:
        f.write(json.dumps(products))
        f.close()
    driver.quit()