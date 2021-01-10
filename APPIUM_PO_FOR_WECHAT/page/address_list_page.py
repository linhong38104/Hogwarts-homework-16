from appium.webdriver.common.mobileby import MobileBy

from APPIUM_PO_FOR_WECHAT.page.base_page import BasePage
from APPIUM_PO_FOR_WECHAT.page.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):
    """
    通讯录PO
    """
    def click_addmember(self):
        """
        添加成员
        :return:
        """
        #self.scroll_find_click("添加成员")
        self.swip_find_click(MobileBy.XPATH,"//*[@text='添加成员']")

        return MemberInviteMenuPage(self.driver)