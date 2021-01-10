from appium.webdriver.common.mobileby import MobileBy

from APPIUM_PO_FOR_WECHAT.page.address_list_page import AddressListPage
from APPIUM_PO_FOR_WECHAT.page.base_page import BasePage


class MainPage(BasePage):

    def goto_address(self):
        """
        进入通讯录
        :return:
        """
        #点击通讯录按钮
        self.find_and_click(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/elq' and @text='通讯录']")
        return AddressListPage(self.driver)