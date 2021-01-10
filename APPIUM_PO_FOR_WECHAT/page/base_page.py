from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.driver = driver

    def find(self,by,locator):
        return self.driver.find_element(by,locator)

    def find_and_click(self,by,locator):
        self.find(by,locator).click()
#滑动慢
    def scroll_find(self,text):
        return self.driver.find_element(MobileBy.
                            ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                 'scrollable(true).instance(0)).'
                                                 'scrollIntoView(new UiSelector().'
                                                 f'text("{text}").instance(0));')

    def swip_find(self, by, locator):
        self.driver.implicitly_wait(1)
        # 找到所有元素
        eles = self.driver.find_elements(by, locator)
        # 不停滑动，直到找到为止
        while len(eles) == 0:
            # 滑动
            self.driver.swipe(0, 600, 0, 400)
            eles = self.driver.find_elements(by, locator)
        self.driver.implicitly_wait(5)
        return eles[0]

    def swip_find_click(self, by, locator):
        self.swip_find(by, locator).click()

    def scroll_find_click(self,text):
        self.scroll_find(text).click()

    def find_and_send(self,by,locator,text):
        self.find(by,locator).send_keys(text)

    def wait_for(self,by,locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((by, locator)))
