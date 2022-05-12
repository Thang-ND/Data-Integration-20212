import time
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
    # dict_product_category = {
    #     "ipad": "https://tiki.vn/search?q=ipad",
    #     "iphone": "https://tiki.vn/search?q=iphone",
    #     "macbook": "https://tiki.vn/search?q=macbook"
    # }

    # RAN_NUM_PAGE = [1, 2] # điền số trang

    # product_ids = []

    # for product_category in dict_product_category:
    #     for num in range(RAN_NUM_PAGE[0], RAN_NUM_PAGE[1] + 1):
    #         driver.get(dict_product_category[product_category] + "&page=" + str(num))
    #         time.sleep(3)
    #         all_product_per_page = driver.find_elements(By.CLASS_NAME, "product-item")
    #         for product in all_product_per_page:
    #             product_ids.append(json.loads(product.get_attribute("data-view-content"))["click_data"]["id"])

    # records = 0

    # with open('/home/sonnh/Documents/THDL/Data-Integration-20212/CrawlData/Mobilecity', 'a+', newline='',encoding='utf-8') as f:
    #     csv_writer = writer(f)
    #     for ids in tqdm(product_ids):
    #         url = "https://tiki.vn/api/v2/products/"+str(ids)
    #         solditems = requests.get(url, headers={"User-Agent": "curl/7.61.0"})
    #         product = solditems.json()
    #         id = product['id']
    #         name = product['name']
    #         short_url = product['short_url']
    #         price = product['price']
    #         original_price = product['original_price']
    #         rating_average = product['rating_average']
    #         review_count = product['review_count']
    #         inventory_status = product['inventory_status']
    #         inventory_type = product['inventory_type']
    #         # all_time_quantity_sold = product['all_time_quantity_sold']
    #         brand_name = ''
    #         if "brand" in product.keys():
    #             brand_name = product['brand']['name']

    #         attributes_dict = {}

    #         for attribute in product['specifications'][0]['attributes']:
    #             attributes_dict[attribute['code']] = attribute['value']

    #         camera_sau = ''
    #         if "camera_sau" in attributes_dict.keys():
    #             camera_sau = attributes_dict['camera_sau']

    #         camera_truoc = ''
    #         if "camera_truoc" in attributes_dict.keys():
    #             camera_truoc = attributes_dict['camera_truoc']

    #         chip_do_hoa = ''
    #         if "chip_do_hoa" in attributes_dict.keys():
    #             chip_do_hoa = attributes_dict['chip_do_hoa']

    #         chip_set = ''
    #         if "chip_set" in attributes_dict.keys():
    #             chip_set = attributes_dict['chip_set']

    #         cpu_speed = ''
    #         if "cpu_speed" in attributes_dict.keys():
    #             cpu_speed = attributes_dict['cpu_speed']

    #         dimensions = ''
    #         if "dimensions" in attributes_dict.keys():
    #             dimensions = attributes_dict['dimensions']

    #         display_type = ''
    #         if "display_type" in attributes_dict.keys():
    #             display_type = attributes_dict['display_type']

    #         origin = ''
    #         if "origin" in attributes_dict.keys():
    #             origin = attributes_dict['origin']

    #         product_weight = ''
    #         if "product_weight" in attributes_dict.keys():
    #             product_weight = attributes_dict['product_weight']

    #         ram = ''
    #         if "ram" in attributes_dict.keys():
    #             ram = attributes_dict['ram']

    #         resolution = ''
    #         if "resolution" in attributes_dict.keys():
    #             resolution = attributes_dict['resolution']

    #         rom = ''
    #         if "rom" in attributes_dict.keys():
    #             rom = attributes_dict['rom']

    #         wifi = ''
    #         if "wifi" in attributes_dict.keys():
    #             wifi = attributes_dict['wifi']
            

    #         csv_writer.writerow([id,name,short_url,price,original_price,rating_average,review_count,inventory_status,inventory_type,brand_name,camera_sau,camera_truoc,chip_do_hoa,chip_set,cpu_speed,dimensions,display_type,origin,product_weight,ram,resolution,rom,wifi,date])
    #         records += 1

    # print("adding "+str(records) + " records")



    urls = []
    products = []
    apple_categories = {
        'iphone': 'https://viettelstore.vn/dtdd-apple-iphone?utm_source=website&utm_medium=sis',
        'ipad': 'https://viettelstore.vn/tablet-apple-ipad?utm_source=website&utm_medium=sis',
        'watch': 'https://viettelstore.vn/tbd-apple-watch?utm_source=website&utm_medium=sis',
        'airpods': 'https://viettelstore.vn/ket-qua-tim-kiem.html?keyword=airpods&utm_source=website&utm_medium=sis'
    }

    for category in apple_categories:    
        driver.get(apple_categories[category])
        items = driver.find_elements(By.CLASS_NAME, 'ProductList3Col_item')
        for i in items:
            urls.append(i.find_element(By.TAG_NAME, 'a').get_attribute('href'))

    for url in tqdm(urls):
        driver.get(url)
        left_row_item = driver.find_elements(By.CLASS_NAME, 'left_row_item')
        right_row_item = driver.find_elements(By.CLASS_NAME, 'right_row_item')

        if (len(left_row_item)>0):
            color_item = driver.find_elements(By.CLASS_NAME,'title-color')
            name = driver.find_element(By.CLASS_NAME,'text2').get_attribute('innerHTML')
            price = driver.find_elements(By.CLASS_NAME, 'txt-24')[1].get_attribute('innerHTML')
                
            colors = []
            for i in color_item:
                colors.append(i.get_attribute('innerHTML'))

            attributes = []
            values = []

            for i in left_row_item:
                attributes.append(i.get_attribute('innerHTML'))
            
            for i in right_row_item:
                values.append(i.get_attribute('innerHTML'))

            product = {}
            product['name'] = name
            product['url'] = url
            product['price'] = price
            product['colors'] = colors
            for i in range(0,len(attributes)):
                product[attributes[i]] = values[i]
            products.append(product)
            
            product['date'] = date

    json_products = json.dumps(products)
    with open("/home/sonnh/Documents/THDL/Data-Integration-20212/CrawlData/ViettelStore/Data.json",'w') as f:
        f.write(json_products)
        f.close()

    driver.quit()