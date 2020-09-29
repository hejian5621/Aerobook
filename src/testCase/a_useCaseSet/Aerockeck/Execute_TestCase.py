
import unittest,time,datetime
from BeautifulReport import BeautifulReport
from config.relative_location import  path
from testCase_set import test_UseCaseSet


"""执行测试用例，生成测试报告"""


# 测试报告名称
file_name=time.strftime("%m%d%H%M%S")+"Aerocheck测试报告"    # 测试报告名称
# 测试报告存放地址
relativeAddress = path.location()
logPath = relativeAddress+"report//Aerocheck//" # 测试报告保存地址
# 用例名称
useCase_name="Aerocheck测试报告"




if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_UseCaseSet))
    result = BeautifulReport(suite).report(filename=file_name,log_path=logPath,description=useCase_name)