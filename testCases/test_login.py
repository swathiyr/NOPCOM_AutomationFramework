import pytest
from selenium import webdriver

from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
#NamingConvention: Test_ID_nameoftestcase


class Test_001_Login():

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_homePageTitle(self,setup):

        self.logger.info("****Testcase_001_Login*****")
        self.logger.info("****Validating Home Page Title*****")
        self.driver = setup
        # Launching application
        self.driver.get(self.baseURL)

        #Returns title of webbrowser
        actual_title = self.driver.title

        #Assertion
        if actual_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****Validating Home Page Title test passed*****")
        else:
            # Method to save screenshots - self.driver.save_screenshot
            # '.' represents current project directory
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("****Validating Home Page Title Failed*****") # Instead of info
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):

        self.logger.info("****Testcase_Login*****")
        self.driver = setup
        #Launching application
        self.driver.get(self.baseURL)
        #creating an object:
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title  # returns title of webbrowser
        self.lp.clickLogout()
        # Returns title of webbrowser
        print(actual_title)
        if actual_title =="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("****Login test is passed*****")
            self.driver.close()
        else:
            # Method to save screenshots - self.driver.save_screenshot
            # '.' represents current project directory
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("****Login test is failed*****") # Instead of info
            assert False