import pytest
from pythoncode.calculator import Calculator


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

    @pytest.mark.parametrize("a,b,expect",[
        (1,2,3),(-1,-2,-3),(100,300,400),(6,6.6,12.6)
    ],ids=["int","minus","bigint","int and float"])
    def test_add(self,a,b,expect):
        assert expect == self.calc.add(a,b)

    @pytest.mark.parametrize("a,b,expect",[
        (2,1,1),(-1,-2,1),(100,300,-200),(6,6.6,-0.6)
    ],ids=["int","minus","bigint","int and float,need to round?"])
    def test_sub(self,a,b,expect):
        assert expect == self.calc.sub(a,b)

    @pytest.mark.parametrize("a,b,expect",[
        (2,1,2),(-1,-2,2),(100,300,30000),(1,0,0),(6,-6.6,-39.6)
    ],ids=["int","minus","bigint","result=0","int and float,need to round?"])
    def test_mul(self,a,b,expect):
        assert expect == self.calc.mul(a,b)

    @pytest.mark.parametrize("a,b,expect",[
        (2,1,2),(-4,-2,2),(600,300,2),(3.6,1.2,3),(1,0,'ERR')
    ],ids=["int","minus","bigint","float","ERR=0"])
    def test_div(self,a,b,expect):
        assert expect == self.calc.div(a,b)