import unittest
from parameterized.parameterized import parameterized
from GenerateTestReports import BeautifulReport

class TestAdd(unittest.TestCase):
  ab=[]
  abc=[]




  # ab=[
  #   ("第一条",1, 1, 2),
  #   ("第二条",2, 2, 4),
  #   ("第三条",3, 3, 6),
  # ]

  abc = [
      ("第一条", 6, 6, 12),
      ("第二条", 7, 7, 14),
      ("第三条", 8, 8, 16),
  ]

  def setUp(self):
      pass


  @parameterized.expand(ab)
  def test1_add(self, name, a, b, c):
     self.assertEqual(a + b, c)


  @parameterized.expand(abc)
  def test2_add(self, name, a, b, c):
      self.assertEqual(a + b, c)





if __name__ == '__main__':
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAdd))
    filename = "/demo_1/testDate"  # 定义个报告存放路径，支持相对路径
    result = BeautifulReport(suite)
    result.report(filename='BeautifulReportTest.html', description='测试deafult报告', log_path=filename)