import time

import pytest
from selenium import webdriver

from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
#NamingConvention: Test_ID_nameoftestcase

class Test_002_DDT_Login():

    baseURL = ReadConfig.getApplicationURL()
    path =".//TestData/LoginData.xlsx"
    #username = ReadConfig.getUseremail() - field is not required since data is provided by excel
    #password = ReadConfig.getpassword() - field is not required since data is provided by excel
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):

        self.logger.info("****Test_002_DDT_Login*****")
        self.driver = setup
        #Launching application
        self.driver.get(self.baseURL)
        #creating an object:
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path,'Sheet1') #returns number of rows
        print("Number of rows in Excel:",self.rows)

        lst_status = []

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp = XLUtils.readData(self.path,'Sheet1',r,3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)


            act_title = self.driver.title
            exp_title ="Dashboard / nopCommerce administration"

            if act_title ==exp_title:
                if self.exp =="Pass":
                    self.logger.info("Testcase passed")
                    time.sleep(5)
                    self.lp.clickLogout()
                    lst_status.append("Pass")

            if act_title ==exp_title:
                if self.exp =="Fail":
                    self.logger.info("Testcase failed")
                    time.sleep(5)
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp =="Pass":
                    self.logger.info("Testcase failed")
                    lst_status.append("Fail")

                elif self.exp =="Fail":
                    self.logger.info("Testcase Passed")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Login DDT test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT test failed")
            self.driver.close()
            assert False

        self.logger.info("****End of Test_002_DDT_Login*****")
        self.logger.info("****Completed Test_002_DDT_Login*****")