from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class InstaBot:
    def __init__(self, username, password):
        driver_path = "C:\webdrivers\chromedriver.exe"
        chrome_options = Options() 
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.instagram.com/")

        #clicking the accept cookies button
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Accept']"))).click()
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button"))).click()  

        time.sleep(2)

        #now insert username and password
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()

        time.sleep(2)

        #click save info and turn on notification
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']"))).click()

        time.sleep(2)
InstaBot("PASS-USERNAME-HERE", "PASSWORD-HERE")
