import random
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
# from bs4 import BeautifulSoup

# """ Lấy content của 1 post """
# def get_post(driver):
#     button = driver.find_element(By.XPATH, '//*[@class="x11i5rnm xat24cr x1mh8g0r x1vvkbs xtlvy1s x126k92a"]')
#     text = button.text
#     print(text)


""" Lấy content của 10 post trong 1 page """
def get_posts(driver, url):

    driver.get(url)
    time.sleep(random.randint(3, 5))



    # Lấy chiều cao của trang
    total_height = driver.execute_script("return document.body.scrollHeight")

    # Tạo vòng lặp để lướt xuống dần dần
    for i in range(1, 10000, 500):
        driver.execute_script("window.scrollTo(0, {});".format(i))
        time.sleep(1)
    driver.execute_script("window.scrollTo(0, {});".format(1))

    element1 = driver.find_element(By.XPATH, '//*[@class="x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x41vudc x6prxxf xvq8zen x1s688f xi81zsa" and text="Phù hợp nhất"]')
   
    element1.click()

    time.sleep(8)

