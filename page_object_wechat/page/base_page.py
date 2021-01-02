import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self,base_driver=None):
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
            self.__cookie_login()
        else:
            self.driver = base_driver

    def __cookie_login(self):
        with open('wetchat.yaml',encoding='UTF-8') as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def find(self,by, value=None):
        #如果传入的是一个元祖，则进行解包元祖传参
        if value is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by=by,value=value)

    def finds(self,by, value=None):
        #如果传入的是一个元祖，则进行解包元祖传参
        if value is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by=by,value=value)

    def quit(self):
        self.driver.quit()