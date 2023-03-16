import tkinter
import os
from tkinter import *


def getListOfAvaialbleTests():
    import fnmatch
    test_dir = "C:\\Users\\sachin.kulkarni\\PycharmProjects\\Internet-Heruko-app-Test\\tests"
    os.system("python --version")
    os.chdir(test_dir)
    print("==============List of tests avaialable================")
    list_of_tests = fnmatch.filter(os.listdir(test_dir), "test_*.py")
    print(list_of_tests)
    test_dict ={}
    for testName in list_of_tests:
        test_dict[testName.replace(".py","")]=testName
    print(test_dict)
    return test_dict









names = getListOfAvaialbleTests()
test_UI = tkinter.Tk()
test_UI.title("Welcome to Automation Test SUites")
test_UI.geometry("500x400")


var ={}

status = []
suites = getListOfAvaialbleTests()
for name in suites.keys():
    stat = []
    var = IntVar()

    test_checkBox=Checkbutton(test_UI,text=name,variable=var )

    test_checkBox.pack()




test_submit_btnn =  tkinter.Button(test_UI,text="Submit",command=print(status))
test_submit_btnn.pack()

print(status)




test_UI.mainloop()
test_UI.quit()









