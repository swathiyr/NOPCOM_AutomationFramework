from selenium import webdriver
class LoginPage:
    textbox_username_id = "Email"
    #typeofdataentry_field_typeoflocator
    textbox_password_id = "Password"
    button_login_xpath = "//input[@class='button-1 login-button']"
    link_logout_linktext ="Logout"

    #Constructor - Directly invoked during object creation:
    def __init__(self,driver):
        self.driver = driver

    #ActionMethod:
    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear() #clear textbox before entering any data
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear() #clear textbox before entering any data
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()