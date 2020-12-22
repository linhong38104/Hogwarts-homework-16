from selenium import webdriver
from selenium.webdriver.common.by import By

from page_object_weixin.page.base_page import BasePage
from page_object_weixin.page.ContactPage import ContactPage


class AddMemberPage(BasePage):  #添加成员操作，可填值
    _location_username= (By.ID, "username")
    _location_acctid = (By.NAME,"acctid")
    _location_add_phone = (By.ID,"memberAdd_phone")
    _location_save = (By.CSS_SELECTOR, ".js_btn_save")

    def add_member(self):#继承base_page
        '''添加成员操作

        :return:
        '''
        #driver = webdriver.Chrome() 避免多窗口创建到base_page中
        self.driver.find_element(*self._location_username).send_keys('TEST02')
        self.driver.find_element(*self._location_acctid).send_keys("TEST02USER")
        self.driver.find_element(*self._location_add_phone).send_keys('13222222222')
        self.driver.find_element(*self._location_save).click()
        return ContactPage(self.driver)

    def add_member_fail(self,accid,phone):
        '''
        添加成员失败操作
        :return:
        '''
        self.driver.find_element(*self._location_username).send_keys('TEST02')
        self.driver.find_element(*self._location_acctid).send_keys(accid)
        self.driver.find_element(*self._location_add_phone).send_keys(phone)
        self.driver.find_element(*self._location_save).click()
       # err_message = self.driver.find_element(By.CSS_SELECTOR,".member_edit_item_right.ww_inputWithTips_WithErr .ww_inputWithTips_tips").text
       # phone_err_message = self.driver.find_element(By.CSS_SELECTOR,".member_edit_item_right.ww_inputWithTips_WithErr .ww_inputWithTips_tips").text
       # error_list = [err_message,phone_err_message]
        #参数化断言

        res = self.finds(By.CSS_SELECTOR,'.ww_inputWithTips_tips')
        print(res)
        error_list = [i.text for i in res]
        return error_list



