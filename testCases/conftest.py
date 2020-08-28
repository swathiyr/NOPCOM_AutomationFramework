import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
        print("launching chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="c:\\geckodriver.exe")
        print("launching firefox browser")
    else:
        driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
    return driver

# get the value from CLI / hook
# this method transfers browser information entered at command prompt to browser(request) method
def pytest_addoption(parser):
    parser.addoption("--browser")

# this will return the browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

########## pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
# adding customized information to the report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Swathi'


# It is hook for delete/Modify Environment info to HTML Report
# method used to delete default information in the HTML report.
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)