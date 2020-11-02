from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class WhatsAppBot:
    def __init__(self):
        driver_path = "C:\webdrivers\chromedriver.exe"

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument(r"user-data-dir=./driver/data")
        driver = webdriver.Chrome(executable_path=driver_path, options=options)
        driver.get('https://web.whatsapp.com/')
        wait = WebDriverWait(driver, 2)

        time.sleep(2)

        message = 'MESSAGE TO BE SENT'

        driver.find_element_by_xpath('//span[@title="CONTACT-NAME-HERE"]')\
            .click()

        time.sleep(2)

        driver.find_element_by_xpath('//div[@data-tab="6"]')\
            .send_keys(message)
        
        time.sleep(2)
        
        send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
        send_button.click()


WhatsAppBot()
