import pytest
from pythoncode.calculator import Calculator
import yaml
import allure

def get_datas():
    with open("./data.yml") as f:
        datas = yaml.safe_load(f)
        add_datas = datas["add_datas"]  # 加法案例数据
        add_ids = datas["myid"]  # 加减法案例解释
        sub_datas = datas["sub_datas"]  # 减法案例数据
        mul_datas = datas["mul_datas"]  # 乘法案例数据
        myid_mul = datas["myid_mul"]  # 乘法案例解释
        div_datas = datas["div_datas"]  # 除法案例数据
        myid_div = datas["myid_div"]  # 除法案例解释
        return [add_datas, add_ids, sub_datas, mul_datas, myid_mul, div_datas, myid_div]

@allure.feature("计算器计算模块")
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

    @allure.story("加法测试模块")
    @pytest.mark.parametrize("a,b,expect",
                             get_datas()[0],
                             ids=get_datas()[1])
    def test_add(self,myfixture,a,b,expect):
        assert expect == self.calc.add(a,b)

    @allure.story("减法测试模块")
    @pytest.mark.parametrize("a,b,expect",
                             get_datas()[2],
                             ids=get_datas()[1])
    def test_sub(self,a,b,expect):
        assert expect == self.calc.sub(a,b)

    @allure.story("乘法测试模块")
    @pytest.mark.parametrize("a,b,expect",get_datas()[3],
                             ids=get_datas()[4])
    def test_mul(self,a,b,expect):
        assert expect == self.calc.mul(a,b)

    @allure.story("除法测试模块")
    @pytest.mark.parametrize("a,b,expect",get_datas()[5],
                             ids=get_datas()[6])
    def test_div(self,a,b,expect):
        assert expect == self.calc.div(a,b)