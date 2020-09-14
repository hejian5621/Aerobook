# 铺层数据库制作



# 铺层库优化工作栏
from ddt import ddt,data
import unittest
from assertpy import assert_that
from config.relative_location import  path
from BeautifulReport import BeautifulReport
import  time
from utils.otherMethods.unittest_start_finish import Initializing




@ddt
class Test_test(unittest.TestCase):
        """铺层数据库制作"""

        global list_dicts

        def __init__(self,*args):
            unittest.TestCase.__init__(self, *args)
            global  number
            global global_UseCase_Name
            global_UseCase_Name=None
            number=0

        @classmethod
        def setUp(self):
            """用例执行前的初始化
               1、首先把需要的文件和模型复制一份出来
            """
            global  number ;global  global_UseCase_Name
            print("测试开始")
            real_UseCase_Name="Test_test"
            number,global_UseCase_Name =Initializing().initialize_globalVariable(number,global_UseCase_Name,real_UseCase_Name)
            print("list_dicts8888:", list_dicts)



        def tearDown(self):
            """用例执行完后收尾
                           1、首先把复制的文件夹删除
            """
            print("测试结束")



        list_dicts=[{"测试点":"b","c":"d"},{"测试点":"2","3":"4"}]
        print("list_dicts111:", list_dicts)
        @data(*list_dicts)  # 参数化参数用例
        def test_1(self,list):
            global number
            expect_result = 1
            actual_result = 2



        list_dicts1 = [{"测试点": "99", "88": "77"}, {"测试点": "66", "88": "33"}]
        print("list_dicts222:", list_dicts1)
        @data(*list_dicts)  # 参数化参数用例
        def test_2(self,list):
            global number
            expect_result = 1
            actual_result = 2
            print("test_2运行第”%r" % number)
            # 断言测试结果
            # assert_that(expect_result).is_equal_to(actual_result)


        def test_3(self):
            global number
            expect_result = 1
            actual_result = 1
            print("test_3运行第”%r" % number)
            # 断言测试结果
            # assert_that(expect_result).is_equal_to(actual_result)


# @ddt
# class Test_test111(unittest.TestCase):
#         """铺层数据库制作"""
#         global list_dicts
#         real_UseCase_Name = "Test_test111"
#
#         def __init__(self, *args):
#             unittest.TestCase.__init__(self, *args)
#             list_dicts = 1
#
#
#
#
#         def setUp(self):
#             """用例执行前的初始化
#                1、首先把需要的文件和模型复制一份出来
#             """
#             global number;global global_UseCase_Name
#
#             print("")
#             print("global_UseCase_Name:", global_UseCase_Name)
#             real_UseCase_Name = "Test_test111"
#             number1,global_UseCase_Name=Initializing().initialize_globalVariable(number, global_UseCase_Name, real_UseCase_Name)
#             print("number=",number1)
#             global_UseCase_Name = real_UseCase_Name
#             print("list_dicts11:", list_dicts)
#             number=number1
#             print("number222", number)
#             print("")
#
#
#
#         print("222")
#         def tearDown(self):
#             """用例执行完后收尾
#                            1、首先把复制的文件夹删除
#             """
#             global number
#             print("tearDown运行第”%r" % number)
#             print("测试结束")
#
#         list_dicts = [{"测试点": "b", "c": "d"}, {"测试点": "2", "3": "4"}, {"测试点": "6", "7": "8"}, {"测试点": "10", "11": "12"}]
#         @data(*list_dicts)  # 参数化参数用例
#         def test_1(self,list):
#             global number
#             print("list:",list)
#             expect_result = 1
#             actual_result = 2
#             print("Test_test1test_1运行第”%r"%number)
#             # # 断言测试结果
#             # assert_that(expect_result).is_equal_to(actual_result)
#
#
#         def test_2(self):
#             global number
#             expect_result = 1
#             actual_result = 1
#             print("test_2运行第”%r" % number)
#             # 断言测试结果
#             # assert_that(expect_result).is_equal_to(actual_result)
#
#
#         def test_3(self):
#             global number
#             expect_result = 1
#             actual_result = 1
#             print("test_3运行第”%r" % number)
#             # 断言测试结果
#             # assert_that(expect_result).is_equal_to(actual_result)






#
# if __name__ == '__main__':
#     unittest.main()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_test))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_test111))
    file_name=time.strftime("%Y%m%d%H%M%S")+"铺层库优化测试报告"    # 测试报告名称
    relativeAddress = path.location()
    logPath = relativeAddress+"report//Aerocheck//laminateOptimize_testReport//" # 测试报告保存地址
    result = BeautifulReport(suite).report(filename=file_name,log_path=logPath,description="铺层库优化工作栏")

