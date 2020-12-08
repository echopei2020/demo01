import ddt
from Common.dataexcel import get_data
import unittest
from selenium import webdriver
import time
excel=get_data('',1)
print(excel)
@ddt.ddt
class Test_se(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.disneyphotopass.com.cn/login.html")
        time.sleep(3)

    @ddt.data(*excel)
    def test_01(self,dic):
        self.driver.find_element_by_id('email').click()
        time.sleep(2)
        self.driver.find_element_by_class_name('login_emails').send_keys(dic.get('username'))
        self.driver.find_element_by_class_name('login_pass').send_keys(dic.get('password'))
        self.driver.find_element_by_class_name('gradient').click()
        time.sleep(3)
        text=self.driver.find_element_by_id('account').text
        print(text)
        assert_word='欢迎 '+dic.get('username')
        print(assert_word)
        self.assertEqual(text,assert_word)

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()


