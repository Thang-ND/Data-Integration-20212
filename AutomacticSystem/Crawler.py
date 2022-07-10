from math import prod
import time
from attr import attrib
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from tqdm import tqdm
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from json import dumps
from kafka import KafkaProducer
import schedule
import time


def run():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x:
                             dumps(x).encode('utf-8'))

    today = time.gmtime()
    date = '{}-{}-{}'.format(today.tm_year,today.tm_mon,today.tm_mday)

    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)

    urls = []
    products = []
    apple_categories = {
        'iphone': 'https://www.xtmobile.vn/apple'
    }

    for category in apple_categories:
        driver.get(apple_categories[category])
        x_path = '/html/body/div[6]/div/div[2]/div[2]/div/div/div[5]/form/a'
        for i in range(0,3):
            driver.find_element(By.XPATH, x_path).click()
            time.sleep(2)

        items = driver.find_element(By.ID,'List_Product').find_elements(By.CLASS_NAME, 'product-info-top')
        for item in items:
            urls.append(item.find_element(By.TAG_NAME,'a').get_attribute('href'))

    for url in tqdm(urls):
        driver.get(url)
        paraexpand = driver.find_element(By.CLASS_NAME, 'paraexpand')

        span = paraexpand.find_elements(By.TAG_NAME,'span')
        strong = paraexpand.find_elements(By.TAG_NAME,'strong')

        attributes = []
        values = []

        for i in span:
            attributes.append(i.get_attribute('innerHTML'))
        for j in strong:
            values.append(j.get_attribute('innerHTML'))

        product = {}

        name = driver.find_element(By.CLASS_NAME, 'name-sp').get_attribute('innerHTML')
        product['name'] = name
        product['url'] = url

        for i in range(0,len(attributes)):
            product[attributes[i]] = values[i]


        color_list_show = driver.find_element(By.CLASS_NAME, 'color-list-show')
        b = color_list_show.find_elements(By.TAG_NAME,'p')
        p = color_list_show.find_elements(By.TAG_NAME,'b')

        color = []
        price = []

        for i in b:
            color.append(i.get_attribute('innerHTML'))
        for i in p:
            price.append(i.get_attribute('innerHTML'))

        for i in range(0,len(color)):
            _product = product.copy()
            _product['color'] = color[i]
            _product['price'] = price[i]
            _product['date'] = date
            products.append(_product)
            producer.send('crawler-apple-product', value=_product)
            print(_product)

    # with open('/home/thanhnv/Code/20212/THDL/Data-Integration-20212/CrawlData/xtmobile/data/Data.json', 'w') as f:
    #     f.write(json.dumps(products))
    #     f.close()
    driver.quit()

if __name__ == '__main__':
    # run()
    schedule.every(10).minutes.do(run())
    while True:
        schedule.run_pending()