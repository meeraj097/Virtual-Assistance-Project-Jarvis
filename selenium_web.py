import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Infow:
    def __init__(self):
        self.query = None
        service = Service(r'C:\Users\meera\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        time.sleep(5)
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        enter.click()

# assist = Infow()
# assist.get_info("neutron stars")
#
# input("Press Enter to close the browser...")

