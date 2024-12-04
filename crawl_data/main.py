import time
import pandas as pd
from dotenv import load_dotenv
from login import login
from get_data import get_posts
import random
import os


def main():
  load_dotenv()

  df_pages = pd.read_csv(r'./pages.csv')

  driver = login(os.getenv("EMAIL_FACEBOOK"),os.getenv("PASSWORD_FACEBOOK"))
  time.sleep(random.randint(8, 10))
  print(">> Login successful")

  # for page_index in range(df_pages.shape[0]):
  for page_index in range(1):
    name = df_pages["name"][page_index]
    url = df_pages["url"][page_index]

    print( ">> Content page", name)

    get_posts(driver, url)


  time.sleep(10)


if __name__ == '__main__':
  main()