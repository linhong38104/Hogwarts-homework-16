from selenium.webdriver.common.by import By

from page_object_wechat.page.base_page import BasePage
from page_object_wechat.page.contact_page import ContactPage


class Add_department_page(BasePage): #添加部门
    _location_name = (By.CSS_SELECTOR,".inputDlg_item [name=name]")
    _location_bus = (By.CSS_SELECTOR,".inputDlg_item a:nth-child(2)")
    _location_sub_bus = (By.CSS_SELECTOR, ".qui_dropdownMenu.ww_dropdownMenu.member_colLeft.js_party_list_container a")
    _location_sure = (By.CSS_SELECTOR, ".qui_dialog_foot.ww_dialog_foot a:nth-child(1)")


    def add_department(self):

        self.driver.find_element(*self._location_name).send_keys("TEST_01") #填写部门名称
        self.driver.find_element(*self._location_bus).click() #点击所属部门下拉框
        self.driver.find_element(*self._location_sub_bus).click() #选择所属部门
        self.driver.find_element(*self._location_sure).click() #点击确定

        return ContactPage(self.driver)

