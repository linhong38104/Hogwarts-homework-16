from appium import webdriver

from APPIUM_PO_FOR_WECHAT.page.base_page import BasePage
from APPIUM_PO_FOR_WECHAT.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
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
        else:
            self.driver.launch_app()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 这里一定要和appium的IP一致，创建连接
        self.driver.implicitly_wait(10)

    def goto_main(self):
        return MainPage(self.driver)