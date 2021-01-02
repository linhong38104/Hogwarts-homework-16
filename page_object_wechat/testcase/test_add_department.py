from page_object_wechat.page.main_page import Mainpage


class Test_add_department:
    def setup_class(self):
        self.main = Mainpage()

    def test_add_department(self):
        #1.跳转通讯录页面 2.添加部门操作 3.添加断言信息，自动跳转到通讯录页面，判断新增的在不在列表中
        res = self.main.goto_content().goto_add_department().add_department().get_department_list()
        assert "TEST_01" in res

    def teardown_class(self):
        self.main.quit()