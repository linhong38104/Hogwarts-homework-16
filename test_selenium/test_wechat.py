from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class Test_wetchat:
    #复用调试
    def test_demo(self):
         #复用已有浏览器
         chrome_arg = webdriver.ChromeOptions()
         chrome_arg.debugger_address = "127.0.0.1:9222"
         driver = webdriver.Chrome(options=chrome_arg)
         #隐式等待5秒
         driver.implicitly_wait(5)
         #登录企业微信
         driver.get("https://work.weixin.qq.com/wework_admin/frame")
         #点击通讯录
         driver.find_element_by_id("menu_contacts").click()
         #点击添加成员 问题：定位不到，可能是JS的原因，继续往下学才晓得
        # click_element = driver.find_element(By.XPATH,'//*[@id="js_contacts114"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]')
         print(driver.get_cookies())

    def test_get_cookie(self):
        #第一步实例化webdriver
        self.driver = webdriver.Chrome()
        #第二步，登录企业微信主页
        self.driver.get("https://work.weixin.qq.com/")
        #点击登录按钮
        self.driver.find_element(By.XPATH,'//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        #定义cookies，并遍历至selenium
        cookies = [{'domain': '.qq.com', 'expiry': 1608221997, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853115057738'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'wmdCOOMsaHJk_-hf8CbFAzZl2PQ0TsrTv2Kc5VSEuKQAivp-7vKmGyVWGyhsIK03E3Fi1P75zI2XYQk4wwKGbzP04cofjDbtmrO-uxRi4ud6-XlDFUO3a4soqOSCTaAkOIDG7C-PGVz2KBpOXGSbgbo4crtddXimUYAYRJXp8MNuYL0Y9VVhu346jfryTW4ZK33tfVBojsfQR8WsxrIXB5kDuWLcoUSphj_fwZ8kdbRCuqmoJip42LxI4ak9vVzKJDdtHh9LqABbAvJHgnymnA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853115057738'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325004205191'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': '5-fUdKe2iIVPMDNAJ-c56XrooW4ljYTc25gKFeserIeBtZZV0xvUXDSWGZVczDcg'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a7232508'}, {'domain': 'work.weixin.qq.com', 'expiry': 1608249403, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '5somuem'}, {'domain': '.qq.com', 'expiry': 1608308337, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1984881728.1608217868'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '1822116981073929'}, {'domain': '.qq.com', 'expiry': 1671293937, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1480351636.1608121288'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639657256, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '8643615744'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639756915, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1608121287,1608121444,1608217888'}, {'domain': '.work.weixin.qq.com', 'expiry': 1610813957, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 2147483537, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '9274228cc32633b596f115be744ed49b0a2b1b61e8c310a1187d2f472cbea6a8'}, {'domain': '.qq.com', 'expiry': 2147483537, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'pGQhQUBHQY'}]
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        #传入cookies后再次登录主页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 点击通讯录
        self.driver.find_element_by_id("menu_contacts").click()