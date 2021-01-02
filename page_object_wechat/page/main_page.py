import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

from page_object_wechat.page.base_page import BasePage
from page_object_wechat.page.contact_page import ContactPage


class Mainpage(BasePage):
    _location_menu_contacts = (By.ID,"menu_contacts")

    def goto_content(self):#跳转通讯录页面
        self.find(self._location_menu_contacts).click() #进入通讯录页面

        return ContactPage(self.driver)
