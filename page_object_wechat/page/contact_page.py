from selenium.webdriver.common.by import By

from page_object_wechat.Test_add_department import Test_add_department
from page_object_wechat.page.base_page import BasePage


class ContactPage(BasePage):
    _location_top_addBtn = (By.CSS_SELECTOR,".member_colLeft_top_addBtn")
    _location_create_party = (By.CSS_SELECTOR,".js_create_party")
    _location_tree_anchor = (By.CSS_SELECTOR,".member_colLeft_bottom .jstree-anchor")

    def goto_add_department(self): #跳转添加部门弹框
        from page_object_wechat.page.add_department_page import Add_department_page

        self.driver.find_element(*self._location_top_addBtn).click() #点击加号
        self.driver.find_element(*self._location_create_party).click() #点击添加部门
        return Add_department_page(self.driver)

    #断言
    def get_department_list(self):
        department_list = self.finds(self._location_tree_anchor)
        print(department_list)
        member_list_res = [i.text for i in department_list]
        print(member_list_res)
        return member_list_res