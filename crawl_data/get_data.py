import csv
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui

def get_comments(driver, url): 
    driver.get(url)
    time.sleep(random.randint(3, 5))

    pyautogui.scroll(-200)
    time.sleep(3)

    a = driver.find_element(By.XPATH, f'//*[@class="x9f619 x1n2onr6 x1ja2u2z xt0psk2 xuxw1ft"]')
    a.click()
    time.sleep(2)


    index = 1
    b = driver.find_elements(By.XPATH,'//*[@class="html-div xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x6s0dn4 x78zum5 x1q0g3np x1iyjqo2 x1qughib xeuugli"]')
    for i in b:
        if index == 3:
            i.click()
        index = index+ + 1
    time.sleep(2)


    scroll = -1000
    scroll_times = 150

    for _ in range(scroll_times):
        pyautogui.scroll(scroll)
        time.sleep(random.randint(2, 3))

    c = driver.find_element(By.XPATH, '//*[@class="html-div x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1gslohp"]')
    d = c.find_elements(By.XPATH, '//*[@class="xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs"]')

    with open('data.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Only write the header if the file is empty
        if file.tell() == 0:
            writer.writerow(['vi_review'])  # Write header

        for i in d:
            k = i.get_attribute('textContent')
            print(k)
            writer.writerow([k])

