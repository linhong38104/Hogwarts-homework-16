import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self,base_driver=None): #构造方法，用于类的初始化，当类被启用时就会执行
        base_driver:WebDriver #注解用，没有实际意义，不是赋值操作，用作IDE的类型提示
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
            self.__cookie_login()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(3)

    def __cookie_login(self):#使用cookie登录
        with open("wetchat.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        # 传入cookies后再次登录主页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def find(self,by,value=None):
        if value is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by=by , value=value)

    def finds(self,by,value=None):
        #如果传入的是一个元祖，则进行解包元祖传参
        if value is None:
            return self.driver.find_elements(*by)
        else:
            #如果传入的是正常定位信息，则正常传参
            return self.driver.find_elements(by=by , value=value)

    def wait_click(self,locator):
        return WebDriverWait(self.driver,9).until(expected_conditions.element_to_be_clickable(locator))

    def quit(self):
        self.driver.quit()