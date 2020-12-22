from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object_weixin.page.base_page import BasePage


class ContactPage(BasePage): #通讯录页面
    _location_member = (By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
    _location_addmember = (By.CSS_SELECTOR,".ww_operationBar .js_add_member")
    def goto_add_member(self):
        from page_object_weixin.page.add_member_page import AddMemberPage  # 循环引用问题
        '''添加成员操作

        '''
        #添加显示等待，保证按钮可以点击
        '''
        WebDriverWait(self.driver,9).until(
            expected_conditions.element_to_be_clickable(self._location_addmember))
        '''
        self.wait_click(self._location_addmember)
        self.find(self._location_addmember).click()
        return AddMemberPage(self.driver)

    def get_member(self):
        '''
        获取成员列表，用来做断言信息

        :return:
        '''
        #member_list获取的webelement对象，需要名字信息
        member_list = self.finds(*self._location_member)
        print(member_list)
        member_list_res = [i.text for i in member_list]
        print(member_list_res)

        '''
        member_list2 = []
        for i in member_list:
            member_list2.append((i.text))
        print(member_list2)
        '''
        return member_list_res