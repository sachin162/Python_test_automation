import inspect

import pytest

from Base_Test_files.test_Selenium_Base_Automation import Base_internet_automation_class
from Pages.internet_heruko_landing import internet_heruko_landing_page

class Test_Internet_Heruko_Landing(Base_internet_automation_class):


    def test_get_links(self):
        land = internet_heruko_landing_page(self.driver)
        all_ele_list = land.get_all_elements()
        land.captureScreenShot()
        print("total number of elements " , len(all_ele_list))

        assert len(all_ele_list) == 44
        print(all_ele_list)
        for ele in all_ele_list:
            print(ele.text)



    def test_AB(self,na):
        land = internet_heruko_landing_page(self.driver)
        all_ele = land.get_all_elements()
        land.clickOnElement(all_ele[0])
        land.getCurrentURL()
        na= inspect.stack()[0][3]
        land.getTextfromElemenet(land.getHeadingAB())
        land.getTextfromElemenet(land.getParaAB())


