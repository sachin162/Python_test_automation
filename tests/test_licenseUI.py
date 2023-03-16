from time import sleep

from selenium import webdriver as wd
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



def test_license():
    chrome_service_obj = Service(
        "C:\\Users\\sachin.kulkarni\\PycharmProjects\\Internet-Heruko-app-Test\\drivers\\110\\chromedriver.exe")
    driver = wd.Chrome(service=chrome_service_obj)

    driver.maximize_window()
    # driver.get("https://magento.softwaretestingboard.com/")
    driver.get("http://licsvr01.rma.lan/license_gen3.0/index.php?i=1")
    driver.find_element(By.XPATH,"//input[@id='username']").send_keys("skulkarni")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Login@123")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/p[6]/a").click()
    driver.find_element(By.XPATH,"//input[@name='exp_type'][2]").click()
    driver.find_element(By.XPATH,"//input[@type='date']").send_keys("04/01/2021")
    sleep(40)
