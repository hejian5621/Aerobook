# 一定要和单元测试框架一起用
import unittest, os
from ddt import ddt, data, unpack, file_data

'''NO.1单组元素'''


# @ddt
# class Testwork(unittest.TestCase):
#
#     @data(1, 2, 3)
#     def test_01(self, value):  # value用来接收data的数据
#         print(value)
#
#
# if __name__ == '__main__':
#     unittest.main()


'''NO.2多组未分解元素'''


@ddt
class Testwork(unittest.TestCase):

    @data([{"title":"2"},{"title":"3"}],[{"title":"2"},{"title":"3"}])
    def test_01(self, value):
        print(value)


if __name__ == '__main__':
    unittest.main()
#
# '''NO.3多组分解元素'''
#
#
# # @ddt
# # class Testwork(unittest.TestCase):
# #
# #     @data((1, 2, 3), (4, 5, 6))
# #     @unpack  # 拆分数据，会根据，号拆分数据
# #     def test_01(self, value1, value2, value3):  # 每组数据有3个值，所以设置3个形参
# #         print(value)
#
#
# if __name__ == '__main__':
#     unittest.main()
