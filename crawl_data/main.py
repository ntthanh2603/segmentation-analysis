import time
import pandas as pd
from dotenv import load_dotenv
from login import login
from get_data import get_comments
import random
import os


def main():
  load_dotenv()

  df_posts = pd.read_csv(r'./posts.csv')

  driver = login(os.getenv("EMAIL_FACEBOOK"),os.getenv("PASSWORD_FACEBOOK"))
  time.sleep(random.randint(8, 10))
  print(">> Login successful")

  for page_index in range(20, df_posts.shape[0]):
    url = df_posts["url"][page_index]
    
    get_comments(driver, url)


  time.sleep(10)


if __name__ == '__main__':
  main()