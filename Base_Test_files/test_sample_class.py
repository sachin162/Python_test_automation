import pytest
from Base_Test_files.test_Selenium_Base_Automation import Base_internet_automation_class
class Test_automation(Base_internet_automation_class):

    def test_gotosdv(self):
        self.driver.get("https://docs.pytest.org/en/7.1.x/explanation/fixtures.html")
