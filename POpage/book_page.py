from Base.base import Base
from selenium.webdriver.common.by import By
import time
class BookPage(Base):
    def book(self):
        return self.findele(By.XPATH,'id("trainListVue")/div[3]/div[1]/div[4]/div[4]/div[2]/div[1]/div[6]'
                                     '/div[1]/a[1]')
    def book_typeD(self):
        re

