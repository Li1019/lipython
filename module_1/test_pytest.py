# =======================
# pytest_prac
# Author : Li
# 2022/04/18
# 19:57
encoding = 'utf-8'
# =======================

# pytest file name: start with test_ OR end with _test
# Test class name: start with Test, NO __init__
# Test method: start with test_
# 断言: assert

# assert, expected behavior, actual behavior

import pytest
import os

# class Test1:
#     def test_01(self):
#         assert 1 == 1
#
#     def test_02(self):
#         assert 2 == 3
#
#
# if __name__ == '__main__':
#     pytest.main([__file__])

# @pytest.fixture()  # 装饰器，所有测试开始之前run的code，setup
# @pytest.fixture(scope='class')  # 装饰器的作用范围
# scope default is function, scope: function, class, module, session
# session level, fixture的内容写到conftest文件里， 同级目录的所有code文件从conftest文件里读取内容
# session: start -> run 同级目录的所有code文件 -> teardown, 作用域: 同级目录的所有code文件
# module: start -> run module -> teardown, 作用域: 当前module
# class: start -> class1 -> teardown -> start -> class2 -> teardown -> ... 作用域: 当前module
# function: start -> funcion1 -> teardown -> start -> function2 -> teardown -> ... 作用域: 当前module
# class:
# def fun1():
#     print('test is starting')
#     yield  # 这之后的代码是teardown, 测试结束以后执行的代码
#     print('test running is done')
#
#
# class Test2:
#     def test_01(self, fun1):
#         assert 1 == 1
#
#     def test_02(self, fun1):
#         assert 1 == 3
#
#
# if __name__ == '__main__':
#     pytest.main([__file__, '-sv'])


# 自动使用setup，teardown
# @pytest.fixture(scope='class', autouse='True')   # 这样，每个测试类的方法里不用写参数fun1
# def fun1():
#     print('test is starting')
#     yield  # 这之后的代码是teardown, 测试结束以后执行的代码
#     print('test running is done')
#
#
# class Test2:
#     def test_01(self):
#         assert 1 == 1
#
#     def test_02(self):
#         assert 1 == 3
#
#
# if __name__ == '__main__':
#     pytest.main([__file__, '-sv'])  # -s, print in pycharm, -sv prints more detail

# scope = session

# class Test2:
#     def test_01(self):
#         assert 1 == 1
#
#     def test_02(self):
#         assert 1 == 3
#
#
# if __name__ == '__main__':
#     pytest.main([__file__, '-sv'])


# data-driven
# class Test3:
#     @pytest.mark.parametrize('result, actual_result', [[1, 1], [1, 2], [3, 3], [4, 5]])  # data-driven
#     def test03(self, result, actual_result):
#         assert result == actual_result
#
#
# if __name__ == '__main__':
#     pytest.main([__file__, '-s'])


# class Test4:
#     @pytest.mark.parametrize('result, actual_result', ([1, 1], [2, 2], [3, 4]))
#     def test04(self, result, actual_result):
#         assert result == actual_result
#
#
# if __name__ == '__main__':
#     pytest.main([__file__, '-s'])

# class Test5:
#     @pytest.mark.parametrize('result, actual_result', ((1, 1), (2, 2), (3, 4)))
#     def test05(self, result, actual_result):
#         assert result == actual_result
#
#
# if __name__ == '__main__':
#     pytest.main([__file__, '-s'])


list_test = [[1, 1], [2, 2], [3, 4]]


class Test6:
    @pytest.mark.parametrize('result,actual_result', list_test)
    def test06(self, result, actual_result):
        assert result == actual_result


if __name__ == '__main__':
    pytest.main([__file__, '-s', '--alluredir', '../report'])
    os.system('allure generate ../report -o ../report/report --clean')
# os.system , it means run command in 