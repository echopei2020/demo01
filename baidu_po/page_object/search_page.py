from selenium import webdriver
from base_page.base import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class SearchPage(BasePage):
    input_el=(By.ID,'kw')
    click_el=(By.ID,'su')
    url='https://www.baidu.com/'
    def input_word(self,txt):
        self.locator(self.input_el).send_keys(txt)

    def click(self):
        self.locator(self.click_el).click()

    def test_search(self,txt):
        self.open()
        self.input_word(txt)
        self.click()
        self.quit()


if __name__=='__main__':
    driver=webdriver.Chrome
    txt='selenium'
    po=SearchPage(driver,SearchPage.url)
    po.test_search(txt)