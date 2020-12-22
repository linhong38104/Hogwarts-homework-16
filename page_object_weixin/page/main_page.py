from selenium.webdriver.common.by import By

from page_object_weixin.page.ContactPage import ContactPage
from page_object_weixin.page.add_member_page import AddMemberPage
from page_object_weixin.page.base_page import BasePage
from selenium import webdriver

class MainPage(BasePage):
    _location_goto_member = (By.CSS_SELECTOR,".ww_indexImg_AddMember")
    _location_menu_contacts = (By.ID, "menu_contacts")
    def goto_add_member(self):#直接跳转添加成员
        '''
        跳转到添加成员页面

        :return:
        '''
        #driver = webdriver.Chrome() 添加到base_page
        self.find(self._location_goto_member).click() # *为解元组操作，将元组中两个值分别解成两个参数传入到方法里面
        return AddMemberPage(self.driver) #结果传输给addmemerpage 实例化

    def goto_contact(self):
        '''跳转到通讯录页面

        :return:
        '''
        self.find(self._location_menu_contacts).click()
        return ContactPage(self.driver)

    def back_main(self):
        self.find(By.ID,"menu_index").click()
        self.find(By.CSS_SELECTOR,"a[node-type='cancel']").click()