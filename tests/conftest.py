import shutil
import time
from datetime import datetime
import os

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

#@pytest.fixture()
def setup_report():
    now = datetime.now()
    current_time = now.strftime("%d_%m_%y_time_%H_%M_%S")
    print("Current Time =", current_time)
    # src_report_path = "C:\\Users\\sachin.kulkarni\\PycharmProjects\\Internet-Heruko-app-Test\\tests\\reports\\"
    src_report_path = os.getcwd()+"\\reports\\"
    #dest_path_report_dir = f"C:\\Users\\sachin.kulkarni\\PycharmProjects\\Internet-Heruko-app-Test\\tests\\reports\\test_report_old_{current_time}\\"
    print(os.listdir(src_report_path))
    f = os.listdir(src_report_path)
    # ti_c = os.path.getctime(os.path.join(src_report_path, f[0]))
    # ti_m = os.path.getmtime(os.path.join(src_report_path, f[0]))
    # c_ti = time.ctime(ti_c).replace(" ","")
    # m_ti = time.ctime(ti_m)

    #print(f"create time : {c_ti} ")
    # dest_path_report_dir = f"C:\\Users\\sachin.kulkarni\\PycharmProjects\\Internet-Heruko-app-Test\\tests\\reports\\report_old_{current_time}"
    dest_path_report_dir =os.getcwd() + f"\\reports\\report_old_{current_time}"
    if len(os.listdir(src_report_path)) == 0:
        print("Running for the first time hence not creating any directory")
        print("reports will be avaialable in ",src_report_path)
    else:
        gen_folder_path = os.mkdir(path=dest_path_report_dir)
    #shutil.copytree(src_report_path, gen_folder_path)
    return src_report_path,dest_path_report_dir

def copy_reports(src_report_path,dest_path_report_dir):
    print("Copy report method SRC",src_report_path)
    print("Copy report method DEST", dest_path_report_dir)
    source = os.listdir(src_report_path)
    for files in source:
        if os.path.isfile(os.path.join(src_report_path, files)):
            src_file_path = src_report_path + files
            dest_fie_path = dest_path_report_dir + files
            print(files)
            shutil.move(src_file_path, dest_fie_path)






@pytest.fixture()
def Setup_Browser(request):
    #files_path = setup_report()
    global driver
    #browserName = request.config.getoption("browser")
    browserName = "chrome"
    if browserName == "chrome":
        #getCurrentChromeVersion_DownloadDriver()
        chrome_service_obj = Service(
            "C:\\Users\\Administrator\\.jenkins\workspace\\chromedriver.exe")
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
    #copy_reports(files_path[0], files_path[1])
    driver.close()
