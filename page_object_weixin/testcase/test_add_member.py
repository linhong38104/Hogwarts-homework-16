import pytest

from page_object_weixin.page.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        #第一次实例化
        self.main = MainPage()

    def test_add_member(self):
        '''通过添加成员测试用例

        :param self:
        :return:
        '''
        #1.跳转添加成员页面 2.添加成员操作 3.添加断言信息，自动跳转到通讯录页面，判断新增的在不在列表中
        res = self.main.goto_add_member().add_member().get_member()
        #拿到信息列表后
        assert "TEST02" in res

    @pytest.mark.parametrize("accid,phone,expect_res",
                             [("TEST02USER","13122222222","该帐号已被“TEST02”占有"),
                              ("TEST03", "13222222222", "该手机已被“TEST02”占有")])
    #第一次参数化传入重复的accid，正确的手机号，断言信息
    #第一次参数化传入正确的accid，重复的手机号，断言信息
    def test_add_member_fail(self,accid,phone,expect_res):
        res = self.main.goto_add_member().add_member_fail(accid,phone)
        assert expect_res in res

    def test_add_member_by_contact(self):
        '''通过通讯录页面添加成员测试用例

        :param self:
        :return:
        '''
        res = self.main.goto_contact().goto_add_member().add_member().get_member()
        assert "TEST02" in res

  #  def teardown(self):
  #      self.main.back_main()

'''
    def teardown_class(self):
        self.main.quit()
'''