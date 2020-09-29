



class save:

    def save_img(self, img_name):  # 错误截图方法，这个必须先定义好
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        import shutil
        import os
        global number
        print("number:" ,number)
        old_path =None
        new_path =None
        if number == 0:
            old_path = r"src/testCase/d_useCase_screenshot/expectScreenshots/1.png"
        elif number == 1:
            old_path = r"src/testCase/d_useCase_screenshot/expectScreenshots/2.png"
        elif number == 2:
            old_path = r"src/testCase/d_useCase_screenshot/expectScreenshots/3.png"
        elif number == 3:
            old_path = r"src/testCase/d_useCase_screenshot/expectScreenshots/4.png"
        elif number == 4:
            old_path = r"src/testCase/d_useCase_screenshot/expectScreenshots/5.png"
        elif number == 5:
            old_path = r"src/testCase/d_useCase_screenshot/expectScreenshots/6.png"
        elif number == 6:
            old_path = r"F:\Aerobook\src\testCase\d_useCase_screenshot\Aerocheck\7.png"
        new_path = r"F:\Aerobook\src\testCase\a_useCaseSet\Aerockeck\img\test_case_1.png"
        print("old_path:", old_path)
        print("new_path:", new_path)
        # filelist = os.listdir(old_path)  # 列出该目录下的所有文件,listdir返回的文件列表是不包含路径的
        shutil.copyfile(old_path, new_path)
        number = number + 1