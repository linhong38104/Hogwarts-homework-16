from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class Test_click:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://sahitest.com/demo/clicks.htm")
    def teardown(self):

        self.driver.quit()

    def test_excute(self):
        click_element = self.driver.find_element(By.XPATH,'/html/body/form/input[3]')
        double_click_element = self.driver.find_element(By.XPATH,'//*[@name="f1"]//input[2]')
        right_click_element = self.driver.find_element(By.XPATH,'/html/body/form/input[4]')

        action = ActionChains(self.driver)
        action.click(click_element)
        action.double_click(double_click_element)
        action.context_click(right_click_element)
        action.perform()

