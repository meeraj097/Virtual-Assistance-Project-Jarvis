from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Music():
    def __init__(self):
        self.query = None
        service = Service(r'C:\Users\meera\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        try:
            # Wait until the first video is clickable
            video = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="contents"]/ytd-video-renderer[1]'))
            )
            video.click()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Close the browser after a certain time for demo purposes
            time.sleep(10)
            self.driver.quit()

# Example usage:
# assist = Music()
# assist.play('shape of you')

# input("Press Enter to close the browser...")
# assist.driver.quit()
