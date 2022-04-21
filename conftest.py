# =======================
# conftest
# Author : Li
# 2022/04/18
# 20:35
encoding = 'utf-8'
# =======================
import pytest


@pytest.fixture(scope='session', autouse='False')
# 这样，每个测试类的方法里不用写参数fun1
def fun1():
    print('test is starting')
    yield  # 这之后的代码是teardown, 测试结束以后执行的代码
    print('test running is done')
