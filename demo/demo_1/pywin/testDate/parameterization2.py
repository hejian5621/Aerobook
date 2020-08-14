import xlrd
import requests
import unittest
import BeautifulReport as bf
import time
import parameterized
import json
path = 'testcase_adapter.xlsx'#定义测试用例名字
testreport = time.strftime('%Y%m%d',time.localtime())#定义测试报告名字
class Op_excel:
    def r_excel(self,path):
        r_workbook = xlrd.open_workbook(path)
        r_sheet = r_workbook.sheets()[0]
        return r_sheet,r_workbook
    #读excel

    def get_nrows(self,r_sheet):
        nrows = r_sheet.nrows
        return nrows

e = Op_excel()#实例化一个操作excel的类的对象
newsheet = e.r_excel(path)[0] #对象调用类的操作读excel方法返回操作的sheet给newsheet
newnrows = e.get_nrows(newsheet) #对象调用类返回行数nrow给newrows
testdata = []
for i in range(1,newnrows): #循环读取excel中的测试用例，把用例加到testdata中生成二维数组
        testdata.append(newsheet.row_values(i))

def reg_receive(url,data,headers): #定义发送的post请求
    r = requests.post(url=url,data=json.dumps(data),headers=headers).json()
    return r



class Test_case(unittest.TestCase):
    @classmethod #类函数，执行测试用例开始前执行
    def setUpClass(cls):
        print('接口测试开始')

    @classmethod #类函数，执行测试用例结束后候执行
    def tearDownClass(cls):
        print('接口测试结束')

    @parameterized.expand(testdata) #testdata是存的excel中的测试case
    def test_reg_receive(self,url,data,headers,expect,desc):
        '''测试用例'''
        self._testMethodName=desc #desc是对用例的描述
        result = reg_receive(url,json.loads(data),json.loads(headers))
        statuscode = result['statusCode'] #返回状态码
        self.assertEqual(int(expect),statuscode) #与测试用例中的状态码进行比对


# unittest.main()
bf = bf.BeautifulReport(unittest.makeSuite(Test_case))
bf.report(filename=testreport,description='接口测试报告')