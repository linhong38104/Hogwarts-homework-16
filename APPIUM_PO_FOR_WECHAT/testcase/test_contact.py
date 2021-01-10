from APPIUM_PO_FOR_WECHAT.page.app import App
from APPIUM_PO_FOR_WECHAT.page.main_page import MainPage


class TestContact:
    def setup_class(self):
        self.app = App()
        self.app.start()
    def test_add_member(self):
        result = self.app.goto_main().goto_address().click_addmember().add_member_manual().add_contact()
        assert result