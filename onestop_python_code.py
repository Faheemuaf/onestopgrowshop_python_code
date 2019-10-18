from selenium import webdriver
from selenium.common import exceptions
import pandas as pd
# path of the driver in which it is installed.
browser = webdriver.Chrome('/home/faheem/PycharmProjects/scrapping_project/chromedriver_linux64/chromedriver')
browser.get('https://www.onestopgrowshop.co.uk/products?keywords=&page=1&utf8=%E2%9C%93')
all_product = browser.find_elements_by_css_selector('div#products.row div')
print(type(all_product))
Name = []
Price = []
i = 1
while i < 5:
    try:
        all_product = browser.find_elements_by_css_selector('div#products.row > div')
        for ball in all_product:
            #print(ball.get_attribute("id"))
            #print(ball.find_element_by_xpath(".//span[@class='info']").text)
            #print(ball.find_element_by_xpath(".//div[@class='panel-footer text-center']").text)
            Name.append(ball.find_element_by_xpath(".//span[@class='info']").text)
            Price.append(ball.find_element_by_xpath(".//div[@class='panel-footer text-center']").text)
        browser.find_elements_by_css_selector('li.next_page')
        i += 1
    except exceptions.StaleElementReferenceException:
        pass
df = pd.DataFrame(list(zip(Price, Name)), columns=['Product Price', 'Product Name'])
all_product_data = df.to_csv('onestop_data.csv', index=False)