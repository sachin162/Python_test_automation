import chromedriver_autoinstaller
import pytest
from selenium.webdriver.chrome.service import Service
import selenium.webdriver as wd



def getCurrentChromeVersion_DownloadDriver():
    currrent_chrome_version = chromedriver_autoinstaller.get_chrome_version()
    print(currrent_chrome_version)
    chromedriver_autoinstaller.install(path="C:\\Users\\sachin.kulkarni\\PycharmProjects\\Internet-Heruko-app-Test\\drivers")
    chromedriver_autoinstaller.install()

getCurrentChromeVersion_DownloadDriver()

@pytest.fixture()
def Setup_Browser(request):
    global driver
    #browserName = request.config.getoption("browser")
    browserName = "chrome"
    if browserName == "chrome":
        getCurrentChromeVersion_DownloadDriver()
        chrome_service_obj = Service(
            "C:\\Users\\sachin.kulkarni\\PycharmProjects\\Internet-Heruko-app-Test\\drivers\\110\\chromedriver.exe")
        driver = wd.Chrome(service=chrome_service_obj)

    elif browserName == "firefox":
        firefox_service_obj = Service("C:\\Users\\sachin.kulkarni\\PycharmProjects\\UI_Test_Automation_Python\\Drivers\\eckodriver.exe")
        driver = wd.Firefox(service=firefox_service_obj)
    else:
        edge_service_obj = Service("C:\\Users\\sachin.kulkarni\\PycharmProjects\\UI_Test_Automation_Python\\Drivers\\msedgedriver.exe")
        driver = wd.Edge(service=edge_service_obj)

    driver.maximize_window()
    #driver.get("https://magento.softwaretestingboard.com/")
    driver.get("https://the-internet.herokuapp.com/")
    request.cls.driver = driver
    yield
    driver.close()