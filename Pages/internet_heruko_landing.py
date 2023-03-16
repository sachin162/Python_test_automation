from selenium.webdriver.common.by import By

from Pages import locators as loc
from Base_Test_files.test_Selenium_Base_Automation import Base_internet_automation_class
from selenium import webdriver as driver
class internet_heruko_landing_page(Base_internet_automation_class):

    def __init__(self, driver):
        global log
        self.driver = driver
        obj = Base_internet_automation_class()
        log = obj.logger_init()

    def get_all_elements(self):
        log.info("Entered to get all the links in Page")
        all_ele = self.driver.find_elements(By.XPATH ,loc.loc_list_of_links)
        log.info("Successfully got all the links in Page")
        return all_ele

    def getHeadingAB(self):
        log.info("Entered to get Heading in AB Page")
        head_ele = self.driver.find_element(By.XPATH, loc.loc_ab_heading)
        return head_ele

    def getParaAB(self):
        log.info("Entered to get Para in AB Page")
        head_ele = self.driver.find_element(By.XPATH, loc.loc_ab_para)
        return head_ele

