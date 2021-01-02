from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_add_department:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        #sleep(10)

    def teardown_class(self):
       #self.driver.quit()
        pass

    def test_get_cookie(self):
        #cookies = self.driver.get_cookies()
        #print(cookies)
        #with open("wetchat.yaml", "w", encoding="UTF-8") as f:
        #    yaml.dump(cookies, f)
        with open('wetchat.yaml',encoding='UTF-8') as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.ID,"menu_contacts").click() #进入通讯录页面
        self.driver.find_element(By.CSS_SELECTOR,".member_colLeft_top_addBtn").click() #点击加号
        self.driver.find_element(By.CSS_SELECTOR,".js_create_party").click() #点击添加部门
        self.driver.find_element(By.CSS_SELECTOR,".inputDlg_item [name=name]").send_keys("TEST_01") #填写部门名称
        self.driver.find_element(By.CSS_SELECTOR,".inputDlg_item a:nth-child(2)").click() #点击所属部门下拉框
        self.driver.find_element(By.CSS_SELECTOR, ".qui_dropdownMenu.ww_dropdownMenu.member_colLeft.js_party_list_container a").click() #选择所属部门
        self.driver.find_element(By.CSS_SELECTOR, ".qui_dialog_foot.ww_dialog_foot a:nth-child(1)").click() #点击确定

    #断言
    