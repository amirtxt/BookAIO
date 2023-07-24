from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from libgen import slibgen
from scihub import req_scihub
import time
import easygui

PATH = (r"C:\Users\Amir\Documents\Downloads\chromedriver.exe")
driver = webdriver.Chrome(PATH)
driver.quit

# options = Options()
# options.add_argument('--headless=new')
# driver = webdriver.Chrome(r"C:\Users\Amir\Documents\Downloads\chromedriver.exe", options=options)         #headless mode

type = easygui.choicebox("","BookAIO",["Book","Paper"])

if type == "Book":
   slibgen()
elif type == "Paper":
   req_scihub()