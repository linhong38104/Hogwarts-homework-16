from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestContact:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "unicodeKeyboard": "true",
            "resetKeyboard": "true",
            "skipDeviceInitialization": "true",
            "skipServerInitialization": "true",
            "noReset": "true",
            "waitForIdleTimeout": 0,
            "ensureWebviewsHavePages":"true"
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 这里一定要和appium的IP一致，创建连接
        self.driver.implicitly_wait(10)

    def test_contact(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/elq' and @text='通讯录']").click()
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'姓名')]/..//*[@text='必填']").send_keys("aaa")
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'性别')]/..//*[@text='男']").click()
        #点开男，当找到元素“女”才触发下一个元素的启动
        #def wait_ele_for(driver : WebDriver):
        #    eles = driver.find_elements(MobileBy.XPATH,"//*[@text='女']")
        #    return len(eles) > 0
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((MobileBy.XPATH, "//*[@text='女']")))
        #WebDriverWait(self.driver,10).until(wait_ele_for)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='女']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'手机')]/..//*[@text='手机号']").send_keys("13482277777")
        self.driver.find_element(MobileBy.XPATH,"//*[@text='保存']").click()

