from Base.base import Base
from selenium.webdriver.common.by import By
import time
class SearchPage(Base):
    def search_leave(self):
        return self.findele(By.ID,'departCityName')
    def search_arrive(self):
        return self.findele(By.ID,'arriveCityName')
    def search_date(self):
        return self.findele(By.ID,'departDate')
    def search_btn(self):
        return self.findele(By.CLASS_NAME,'searchbtn')
    def search_js(self,value):
        jsvalue="document.getElementById('departDate').value='%s'"%(value)

    def search_train(self,leave,arrive,leave_date):
        self.search_leave().send_keys(leave)
        time.sleep(2)
        self.search_arrive(arrive)
        self.search_js(leave_date)
        self.search_btn().click()
        time.sleep(4)
        return self.url()