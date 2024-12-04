import random
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from bs4 import BeautifulSoup

# """ Lấy content của 1 post """
# def get_post(driver):
#     button = driver.find_element(By.XPATH, '//*[@class="x11i5rnm xat24cr x1mh8g0r x1vvkbs xtlvy1s x126k92a"]')
#     text = button.text
#     print(text)


""" Lấy content của 10 post trong 1 page """
def get_posts(driver, url):
    driver.get(url)
    time.sleep(random.randint(3, 5))

    # elements = driver.find_elements(By.XPATH, '//*[@class="html-div xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd"]')
    # time.sleep(random.randint(5, 8))
    # print(elements)

    # for index in range(3):
    #     # get_post(elements[index])
    #     time.sleep(random.randint(1, 2))
        # print(elements[index].text)

    # Lấy chiều cao của trang
    total_height = driver.execute_script("return document.body.scrollHeight")

    # Tạo vòng lặp để lướt xuống dần dần
    for i in range(1, 2000, 500):
        driver.execute_script("window.scrollTo(0, {});".format(i))
        time.sleep(1)
    driver.execute_script("window.scrollTo(0, {});".format(1))

    elements = driver.find_elements(By.XPATH, '//span[@dir="auto" and @class="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h"]')
    # elements = driver.find_elements(By.CLASS_NAME, 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h')
    time.sleep(random.randint(3, 5))

    print(elements[5].get_attribute('outerHTML'))

    # dom_content = elements[10].get_attribute('outerHTML')

    # print(dom_content)
    # time.sleep(random.randint(3, 5))

