import inspect
import os
import random
from datetime import datetime

import pytest
from selenium import webdriver
import chromedriver_autoinstaller
import logging

currrent_chrome_version = chromedriver_autoinstaller.get_chrome_version()
chromedriver_autoinstaller.install()
log_dir_path ="C:\\Users\\sachin.kulkarni\\PycharmProjects\\Internet-Heruko-app-Test\\tests\\log_files"
@pytest.mark.usefixtures("Setup_Browser")
class Base_internet_automation_class:

    def takeScreenShot(self):
        self.driver.save_screenshot("ss.png")
    def getCurrentURL(self):
        print(self.driver.current_url)
    def clickOnElement(self,Webelement):
        Webelement.click()

    def getTextfromElemenet(self,webelement):
        print(webelement.text)


    def captureScreenShot(self):
        self.driver.get_screenshot_as_file(f"C:\\Users\\sachin.kulkarni\\PycharmProjects\\Internet-Heruko-app-Test\\Base_Test_files\\sachin.png")

    def getCurrentChromeVersion_DownloadDriver(self):
        currrent_chrome_version = chromedriver_autoinstaller.get_chrome_version()
        chromedriver_autoinstaller.install()

    def logger_init(self, type=None):
        now = datetime.now()
        current_time = now.strftime("%d_%m_%y_time_%H_%M_%S")
        print("Current Time =", current_time)
        rdno = random.randint(1, 100)
        current_min = now.strftime(f"%d_%m_%y_time")
        print(current_min)
        dir = os.getcwd()
        file = os.path.basename(__file__)
        print(file)
        print(dir)
        print(f"{dir}\\screenshots\\{current_min}")
        calledMethodName = inspect.stack()[1][3]
        callerFileName = inspect.stack()[1][1].split("\\")[-1]
        print(inspect.stack()[1][1])
        fileName = os.path.basename(__file__)
        logger = logging.getLogger(calledMethodName)
        os.chdir(log_dir_path)
        fh = logging.FileHandler(f"Test_log_{current_min}.txt","w")
        log_format = logging.Formatter("%(asctime)s : %(levelname)s : %(funcName)s: %(message)s  ")
        fh.setFormatter(log_format)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(fh)
        logger.info(inspect.stack()[1][1])
        return logger




