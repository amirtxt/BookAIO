from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time
import easygui

PATH = (r"C:\Users\Amir\Documents\Downloads\chromedriver.exe")
driver = webdriver.Chrome(PATH)

def req_scihub():
    doi = easygui.enterbox("DOI?")
    driver.get(f"https://sci-hub.se/{doi}")
    time.sleep(10)
   #  search.send_keys(Keys.RETURN)
   #  time.sleep(2)
   #  download = driver.find_element(By.ID, value="button")                 download button not accessible through html
   #  download.send_keys(Keys.RETURN)
   #  time.sleep(10)