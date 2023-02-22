from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By


chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
service_obj=Service("Chromedriver/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj, options=chrome_options)
driver.maximize_window()

def RunSearchTest(search_string):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.ID, "searchBar").send_keys(search_string)
    time.sleep(3)

    driver.find_element(By.ID, "submit").click()

time.sleep(3)

RunSearchTest("american")

time.sleep(3)

RunSearchTest("am")

time.sleep(3)

RunSearchTest("american gothic")

time.sleep(3)

RunSearchTest("AMERICAN GOTHIC")

time.sleep(3)

RunSearchTest("aMerIcan GOtHic")




