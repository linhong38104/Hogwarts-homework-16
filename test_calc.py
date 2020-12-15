import pytest
from pythoncode.calculator import Calculator
import yaml

class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("计算程序开始测试")
    def teardown_class(self):
        print("计算程序测试结束")
    def setup_method(self):
        print("开始计算")
    def teardown_method(self):
        print("结束计算")


    @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("./data.yml"))["add_datas"],
                             ids=yaml.safe_load(open("./data.yml"))["myid"])
    def test_add(self,a,b,expect):
        assert expect == self.calc.add(a,b)


    @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("./data.yml"))["sub_datas"],
                             ids=yaml.safe_load(open("./data.yml"))["myid"])
    def test_sub(self,a,b,expect):
        assert expect == self.calc.sub(a,b)

    @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("./data.yml"))["mul_datas"],
                             ids=yaml.safe_load(open("./data.yml"))["myid_mul"])
    def test_mul(self,a,b,expect):
        assert expect == self.calc.mul(a,b)

    @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("./data.yml"))["div_datas"],
                             ids=yaml.safe_load(open("./data.yml"))["myid_div"])
    def test_div(self,a,b,expect):
        assert expect == self.calc.div(a,b)