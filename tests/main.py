import os
import sys

from conftest import setup_report
from conftest import copy_reports
import pytest
import fnmatch
test_dir ="C:\\Users\\sachin.kulkarni\\PycharmProjects\\Internet-Heruko-app-Test\\tests"
test_dir=os. getcwd()
os.system("python --version")
os.chdir(test_dir)
print("==============List of tests avaialable================")
list_of_tests = fnmatch.filter(os.listdir(test_dir),"test_*.py")
print(list_of_tests)

print("=======================================================")

# inp = int(input("Enter the "
#       "1. to run a single suite "
#       "2. To run Multiple Suites "
#       "3. To run all test suites "
#       "4. Exit"))

# files_path = setup_report()
# report_path = files_path[1]

# if inp==1:
#     suiteName = input("Enter the Name of the suite ")
#     print(report_path)
#     pytest_result_code = os.system(f"pytest {suiteName} --alluredir={report_path}")
#     if pytest_result_code == 0:
#         print("printing the allure generate system call OP", os.system(f"allure generate {report_path} --clean "))
#         # report_name = "C:\\Users\sachin.kulkarni\PycharmProjects\Internet-Heruko-app-Test\tests\allure-report\index.html"
#         os.system("start chrome http://localhost:63342/Internet-Heruko-app-Test/tests/allure-report/index.html")
#     else:
#         print("Unable to generate report some error in running the test")
#         sys.exit(1)
# elif inp==2:
#     suiteNames = input("Enter the suite names seperated by ',''")
#     list_of_suites = suiteNames.split(",")
#     print(list_of_suites)
#     for suite in list_of_suites:
#         pytest_result_code = os.system(f"pytest {suite} --alluredir={report_path}")
#         if pytest_result_code == 0:
#             print("printing the allure generate system call OP", os.system(f"allure generate {report_path} --clean "))
#             # report_name = "C:\\Users\sachin.kulkarni\PycharmProjects\Internet-Heruko-app-Test\tests\allure-report\index.html"
#             os.system("start chrome http://localhost:63342/Internet-Heruko-app-Test/tests/allure-report/index.html")
#         else:
#             print("Unable to generate report some error in running the test")
#             sys.exit(1)
# elif inp==3:
#     print("Selected all suites to run ")
#     pytest_result_code = os.system(f"pytest  --alluredir={report_path}")
#     if pytest_result_code == 0:
#         print("printing the allure generate system call OP", os.system(f"allure generate {report_path} --clean "))
#         # report_name = "C:\\Users\sachin.kulkarni\PycharmProjects\Internet-Heruko-app-Test\tests\allure-report\index.html"
#         os.system("start chrome http://localhost:63342/Internet-Heruko-app-Test/tests/allure-report/index.html")
#     else:
#         print("Unable to generate report some error in running the test")
#         sys.exit(1)
# else:
#     print("Exiting the Test run")
#     sys.exit(1)
parser = argparse.ArgumentParser()
parser.add_argument("--run_option",type=int)
parser.add_argument("--suiteName",type=str)
inp = parser.parse_args()
# parser.add_argument()
print(inp.run_option)
print(type(inp.run_option))

files_path = setup_report()
report_path = files_path[1]

if inp.run_option==1:
    print(inp.suiteName)
    print(type(inp.suiteName))
    suiteName = inp.suiteName
    print(report_path)
    pytest_result_code = os.system(f"pytest {suiteName} --alluredir={report_path}")
    if pytest_result_code == 0:
        print("printing the allure generate system call OP", os.system(f"allure generate {report_path} --clean "))
        # report_name = "C:\\Users\sachin.kulkarni\PycharmProjects\Internet-Heruko-app-Test\tests\allure-report\index.html"
        os.system("start chrome http://localhost:63342/Internet-Heruko-app-Test/tests/allure-report/index.html")
    else:
        print("Unable to generate report some error in running the test")
        sys.exit(1)
elif inp.run_option==2:
    print(inp.suiteName)
    print(type(inp.suiteName))
    suiteName = inp.suiteName
    suiteNames = input("Enter the suite names seperated by ',''")
    list_of_suites = suiteNames.split(",")
    print(list_of_suites)
    for suite in list_of_suites:
        pytest_result_code = os.system(f"pytest {suite} --alluredir={report_path}")
        if pytest_result_code == 0:
            print("printing the allure generate system call OP", os.system(f"allure generate {report_path} --clean "))
            # report_name = "C:\\Users\sachin.kulkarni\PycharmProjects\Internet-Heruko-app-Test\tests\allure-report\index.html"
            os.system("start chrome http://localhost:63342/Internet-Heruko-app-Test/tests/allure-report/index.html")
        else:
            print("Unable to generate report some error in running the test")
            sys.exit(1)
elif inp.run_option==3:
    print("Selected all suites to run ")
    pytest_result_code = os.system(f"pytest  --alluredir={report_path}")
    if pytest_result_code == 0:
        print("printing the allure generate system call OP", os.system(f"allure generate {report_path} --clean "))
        # report_name = "C:\\Users\sachin.kulkarni\PycharmProjects\Internet-Heruko-app-Test\tests\allure-report\index.html"
        os.system("start chrome http://localhost:63342/Internet-Heruko-app-Test/tests/allure-report/index.html")
    else:
        print("Unable to generate report some error in running the test")
        sys.exit(1)
else:
    print("Exiting the Test run")
    sys.exit(1)

# print(report_path)
# pytest_result_code = os.system(f"pytest --alluredir={report_path}")
# if pytest_result_code==0:
#     print("printing the allure generate system call OP", os.system(f"allure generate {report_path} --clean "))
#     # report_name = "C:\\Users\sachin.kulkarni\PycharmProjects\Internet-Heruko-app-Test\tests\allure-report\index.html"
#     os.system("start chrome http://localhost:63342/Internet-Heruko-app-Test/tests/allure-report/index.html")
# else:
#     print("Unable to generate report some error in running the test")
#     sys.exit(1)


# #http://localhost:63342/Internet-Heruko-app-Test/tests/allure-report/index.html
# os.system(f"allure generate reports --clean")


