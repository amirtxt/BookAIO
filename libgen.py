from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time
import easygui

PATH = (r"C:\Users\shark\Downloads\chromedriver.exe")
driver = webdriver.Chrome(PATH)

# options = Options()
# options.add_argument('--headless=new')
# driver = webdriver.Chrome(r"C:\Users\Amir\Documents\Downloads\chromedriver.exe", options=options)    #headless mode

def slibgen():
    driver.get("https://libgen.is/")
    btitle = easygui.enterbox("Book Title?")

    search = driver.find_element(By.ID, value= "searchform")
    search.send_keys(btitle)
    search.send_keys(Keys.RETURN)
    time.sleep(1)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "[1]"))
        )
    except:
        print("None found")
        time.sleep(1)
        driver.quit()

    link = driver.find_element(By.LINK_TEXT, value = "[1]")
    link.send_keys(Keys.RETURN)

    time.sleep(2)


    download = driver.find_element(By.LINK_TEXT, value = "GET")
    download.send_keys(Keys.RETURN)

