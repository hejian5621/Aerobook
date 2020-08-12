import time
from BeautifulReport import BeautifulReport
import unittest

'''指定测试用例为当前文件夹下的interface_case_msg目录'''
test_dir = './test'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './test/' + now + '_result.html'
    fp = open(filename, 'wb')
    BeautifulReport(discover).report(description='测试', filename=filename)
    fp.close()