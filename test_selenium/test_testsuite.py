
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestTestsuite():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    #设置隐式等待
    self.driver.implicitly_wait(10)
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testsearch(self):
    self.driver.get("https://www.baidu.com/")
    self.driver.set_window_size(1918, 707)
    self.driver.find_element(By.ID, "kw").send_keys("helloworld")
    self.driver.find_element(By.ID, "su").click()


    self.driver.close()
  
