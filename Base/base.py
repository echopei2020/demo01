from Common.log import FrameLog
from selenium import webdriver
class Base():
    def __init__(self,driver):
        self.driver=driver
        self.log=FrameLog().log()

    def findele(self,*args):
        try:
            print(args)
            self.log.info("通过"+args[0]+"定位，元素是"+args[1])
            return self.driver.find_element(*args)
        except:
            self.log.error("定位元素失败")

    def click(self,args):
        self.findele(args).click()

    def sendkey(self,args,value):
        self.findele(args).send_keys(value)

    def js(self,str):
        self.driver.execute_script(str)

    def url(self):
        return self.driver.current_url

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def quit(self):
        self.driver.quit()

