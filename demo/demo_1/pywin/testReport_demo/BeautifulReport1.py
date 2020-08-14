import unittest
import time

from BeautifulReport import BeautifulReport



class Test_UseCaseSet(unittest.TestCase):
    """测试类"""






    def setUp(self):
        """
        初始值
        """
        # 链接警告窗口
        # global app ;global Text
        # Text=None
        # app = Application().connect(title_re="警告")
        pass


    def test_1tearDown(self):
        """
         测试小程序能否用电话号码登录
        """
        global Text
        # dlg_spec = app.window(title="警告")
        # # dlg_spec.capture_as_image().save("F:\\Aerobook\\src\\testCase\\useCase_screenshot\\Aerocheck1\\word.png")
        # Text=picture_text(None).screenshot("F:\\Aerobook\\src\\testCase\\useCase_screenshot\\Aerocheck1\\word.png")
        # print("Text", Text)
        self.assertEqual("铺层数据库为空KO", "铺层数据库为空KO")  # 是字典的类型

    def test_2tearDown(self):
        """
         测试小程序能否用电话号码登录
        """
        global Text
        # dlg_spec = app.window(title="警告")
        # # dlg_spec.capture_as_image().save("F:\\Aerobook\\src\\testCase\\useCase_screenshot\\Aerocheck1\\word.png")
        # Text=picture_text(None).screenshot("F:\\Aerobook\\src\\testCase\\useCase_screenshot\\Aerocheck1\\word.png")
        # print("Text", Text)
        self.assertEqual("铺层数据库为空K", "铺层数据库为空KO")  # 是字典的类型
        self.assertEqual("a", "b")  # 是字典的类型

    def tearDown(self):
        """
        :return:
        """
        print("结束测试")








if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_UseCaseSet))
    filename = "F:\\Aerobook\\demo\\demo_1\\pywin\\testReport_demo"  # 定义个报告存放路径，支持相对路径
    result = BeautifulReport(suite)
    result.report(filename='BeautifulReportTest.html', description='测试deafult报告', log_path=filename)