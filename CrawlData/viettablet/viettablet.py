from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.viettablet.com/iphone'
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get(url)
driver.implicitly_wait(25)
button_locator = (By.XPATH, '//*[@id="category_products_11"]/a')
button = driver.find_element(*button_locator)
button.click()
driver.implicitly_wait(25)


for i in range(5):
    button2_locator = (By.XPATH, '//*[@id="danhmuc_116"]/a')
    button2 = driver.find_element(*button2_locator)
    button2.click()
    driver.implicitly_wait(25)
print("start find elements")
final_res = []
link_locator = (By.XPATH, '//a[@class="product-title"]')
result = driver.find_elements(*link_locator)

f = open("./url.txt", "w")
for res in result: 
    f.write(res.get_property("href"))
    f.write("\n")
f.close()


# Button: //*[@id="category_products_11"]/a 
# //*[@id="danhmuc_116"]/a
# //*[@id="danhmuc_116"]/a
# //*[@id="danhmuc_116"]/a
# //*[@id="danhmuc_116"]/a
# //*[@id="danhmuc_116"]/a
