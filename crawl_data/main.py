import time
import pandas as pd
from dotenv import load_dotenv
from login import login
import os


def main():
  load_dotenv()

  df_pages = pd.read_csv(r'./pagenames.csv')
  
  print(df_pages)

  # driver = login(os.getenv("EMAIL_FACEBOOK"),os.getenv("PASSWORD_FACEBOOK"))
  driver = login("k67ai2@gmail.com","devkhongbug")
  

   

  print(driver)
    

  time.sleep(10)


if __name__ == '__main__':
  main()