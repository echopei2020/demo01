from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
class BasePage():
    def __init__(self,driver,url):
        self.driver = webdriver.Chrome()
        self.url=url

    def locator(self,ele):
        return self.driver.find_element(*ele)
    def open(self):
        self.driver.get(self.url)

    def quit(self):
        sleep(2)
        self.driver.quit()