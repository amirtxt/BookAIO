from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from libgen import slibgen
import time
import easygui

PATH = (r"C:\Users\Amir\Documents\Downloads\chromedriver.exe")
driver = webdriver.Chrome(PATH)
driver.quit

options = Options()
options.add_argument('--headless=new')
driver = webdriver.Chrome(r"C:\Users\Amir\Documents\Downloads\chromedriver.exe", options=options)

type = easygui.choicebox("","BookAIO",["Book","Paper"])

if type == "Book":
   slibgen()
elif type == "Paper":
    driver.get("https://sci-hub.se/")
    search = driver.find_element(By.ID, value="request")
    search.send_keys("https://doi.org/10.1016/j.econedurev.2013.08.001")
    time.sleep(1)
    search.send_keys(Keys.RETURN)
    time.sleep(2)
    download = driver.find_element(By.ID, value="button")       #download button can't be seen in the main html
    download.send_keys(Keys.RETURN)
    time.sleep(10)