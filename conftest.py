import pytest
@pytest.fixture(params=["fixture第一次","fixture第二次"])
def myfixture(request):
    print("执行testPytest里的前置函数，%s" % request.param)
    yield request.param
    print("fixture运行结束")