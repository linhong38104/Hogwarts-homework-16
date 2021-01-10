from appium.webdriver.common.mobileby import MobileBy

from APPIUM_PO_FOR_WECHAT.page.base_page import BasePage


class ContactAdd(BasePage):
    """
    成员信息编辑
    """
    def add_contact(self):
        """
        添加信息
        :return:
        """
        #todo 姓名，性别，手机号填写

        self.find_and_send(MobileBy.XPATH,"//*[contains(@text,'姓名')]/..//*[@text='必填']","aaa")
        self.find_and_click(MobileBy.XPATH,"//*[contains(@text,'性别')]/..//*[@text='男']")
        #点开男，当找到元素“女”才触发下一个元素的启动
        #def wait_ele_for(driver : WebDriver):
        #    eles = driver.find_elements(MobileBy.XPATH,"//*[@text='女']")
        #    return len(eles) > 0
        self.wait_for(MobileBy.XPATH, "//*[@text='女']")
        #WebDriverWait(self.driver,10).until(wait_ele_for)
        self.find_and_click(MobileBy.XPATH,"//*[@text='女']")
        self.find_and_send(MobileBy.XPATH,"//*[contains(@text,'手机')]/..//*[@text='手机号']","13482277777")
        self.find_and_click(MobileBy.XPATH,"//*[@text='保存']")
        return "TRUE"